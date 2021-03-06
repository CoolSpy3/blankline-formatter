import os
import re
import sys

path = ''
supportedFiletypes = []

if len(sys.argv) < 2:
    print('Usage: format.py [target directory] [supported filetypes]')
else:
    path = sys.argv[1]
    sys.argv.pop(0)
    sys.argv.pop(0)
    filetypePattern = re.compile(r'((.*)\.)?([^\.]+)')
    for t in sys.argv:
        supportedFiletypes.append(filetypePattern.match(t).group(3))

for root, dirs, files in os.walk(path):
    for filename in files:
        isSupported = False
        for filetype in supportedFiletypes:
            if filename.endswith('.' + filetype):
                isSupported = True
                break
        if not isSupported:
            continue
        lines = []
        with open(os.path.join(root, filename),'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                if line[-1] == '\n':
                    line = line[:-1]
                lines.append(line)

        with open(os.path.join(root, filename),'w') as file:
            for i, line in enumerate(lines):
                if not line.isspace():
                    file.write(line)
                if not line.isspace() or len(lines)-1 != i:
                    file.write('\n')
