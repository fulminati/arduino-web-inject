##
# Arduino Web Inject
#
# Inject and build web files into your sketches.
#
# Copyright (c) 2020 Francesco Bianco <bianco@javanile.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##

import asyncio
import glob
import re 
import os

from watchfiles import awatch
from csscompressor import compress
from jsmin import jsmin
from htmlmin import minify 
from binaryornot.check import is_binary

__version__ = '0.1.22'

watch_dir = 'tests/fixtures'
watch_ext = ('.cpp', '.h', '.c')

ignore_ext = ('.lock')

print("Start watch")

def get_files():
    files = []
    for ext in watch_ext:
        pattern = watch_dir + '/**/*' + ext
        files.extend(glob.glob(pattern, recursive=True))
    return files

def stringify(code):
    code = re.sub(r'"', r'\"', code)
    code = re.sub(r'\{\{ ([a-z]+) \}\}', r'" + \g<1> + "', code)
    return '"' + code + '"'

def inject(file):    
    def replace(lines):
        inject_file = os.path.dirname(file) + "/" +lines.group(2)
        inject_type = lines.group(3);        
        code = '"Problem with file: ' + inject_file + '"';        
        if os.path.exists(inject_file):            
            inject_file = os.path.abspath(inject_file);
            print("Inject: " + inject_file)
            if inject_type != "String" or is_binary(inject_file):
                with open(inject_file, "rb") as f:
                    bytes = []
                    byte = f.read(1)
                    while byte != b"":                    
                        bytes.append(f'0x{ord(byte):02x}')
                        byte = f.read(1)                
                    code = '{' + ', '.join(bytes) + '}'
            else:
                with open(inject_file, "r") as f:
                    code = f.read()
                    if inject_file.lower().endswith('.js'): 
                        code = jsmin(code)
                    elif inject_file.lower().endswith('.css'): 
                        code = compress(code)
                    elif inject_file.lower().endswith('.html'): 
                        code = minify(code, remove_comments=True, remove_empty_space=True)            
                    code = stringify(code);
        return lines.group(1) + ' ' + code + ';'
    return replace

def parse(file):
    pattern = r'(// @inject "([A-Za-z0-9./-_]+)"\nconst ([A-Za-z0-9 ]+) ([A-Za-z0-9]+)(\[\])? =)(.*);'
    with open(file, "r") as f:
        source = f.read()                   
        change = re.sub(pattern, inject(file), source, flags = re.MULTILINE)
        print("Update: " + file)
        if source != change:
            with open(file, "w") as f: f.write(change)        
            with open(file + '.lock', 'a'): pass
    
def build():
    for file in get_files():
        parse(os.path.abspath(file))
        
async def watch():
    async for changes in awatch(watch_dir):        
        for val in changes:
            file = val[1];
            if file.lower().endswith(ignore_ext):
                continue
            elif os.path.exists(file + '.lock'):
                os.remove(file + '.lock')
            else:                        
                print("Change: " + file);            
                build()

def main():
    asyncio.run(watch())

if __name__ == '__main__':
    main()
