import asyncio
import glob
import re 

from watchfiles import awatch

watch_dir = 'tests/fixtures'
watch_ext = ['cpp', 'h', 'c']

print("Start watch")

def get_files():
    files = []
    for ext in watch_ext:
        pattern = watch_dir + '/**/*.' + ext
        files.extend(glob.glob(pattern, recursive=True))
    return files

def inject(lines):
    #print("a: "+ lines.group(2))
    file = lines.group(2)
    code = "";
    with open(file) as f:
        code = f.read()                       
    return lines.group(1) + ' "' + code + '";'

def parse(file):
    print(file)
    pattern = r'(// @inject "([a-z./]+)"\nString ([a-z]+) =)(.*);'
    with open(file) as f:
        code = f.read()                   
        code = re.sub(pattern, inject, code, flags = re.MULTILINE)
        print(code)
    
def build():
    for file in get_files():
        parse(file)
        

build()

"""
async def main():
    async for changes in awatch(watch_dir):        
        for val in changes:
            print(val[0], val[1])

asyncio.run(main())
"""


