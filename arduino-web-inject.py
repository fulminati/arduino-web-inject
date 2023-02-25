import asyncio
import glob
import re 
import os

from watchfiles import awatch
from csscompressor import compress
from jsmin import jsmin
from htmlmin import minify 

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

def inject(lines):    
    file = lines.group(2)
    code = "Problem with file: " + file;
    if os.path.exists(file):
        with open(file) as f:
            code = f.read()
            if file.lower().endswith('.js'):                
                code = jsmin(code)
            elif file.lower().endswith('.css'):                
                code = compress(code)
            elif file.lower().endswith('.html'):                
                code = minify(code, remove_comments=True)
    return lines.group(1) + ' ' + stringify(code) + ';'

def parse(file):
    pattern = r'(// @inject "([a-z./]+)"\nString ([a-z]+) =)(.*);'
    with open(file, "r") as f:
        source = f.read()                   
        change = re.sub(pattern, inject, source, flags = re.MULTILINE)
        if source != change:
            print("Update: " + file)
            with open(file, "w") as f: f.write(change)        
            with open(file + '.lock', 'a'): pass
    
def build():
    for file in get_files():
        parse(file)
        
async def main():
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
            #print(val[0], val[1])

asyncio.run(main())

