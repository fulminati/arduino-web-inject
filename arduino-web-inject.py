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

def inject(file):    
    def replace(lines):
        inject_file = os.path.dirname(file) + "/" +lines.group(2)
        code = "Problem with file: " + inject_file;
        if os.path.exists(inject_file):
            inject_file = os.path.abspath(inject_file);
            print("Inject: " + inject_file)
            with open(inject_file) as f:
                code = f.read()
                if inject_file.lower().endswith('.js'): 
                    code = jsmin(code)
                elif inject_file.lower().endswith('.css'): 
                    code = compress(code)
                elif inject_file.lower().endswith('.html'): 
                    code = minify(code, remove_comments=True, remove_empty_space=True)
        return lines.group(1) + ' ' + stringify(code) + ';'
    return replace

def parse(file):
    pattern = r'(// @inject "([a-z./]+)"\nString ([a-z]+) =)(.*);'
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

asyncio.run(main())

