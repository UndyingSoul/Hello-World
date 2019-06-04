#!/usr/bin/env python3
#Found here: https://github.com/leachim6/hello-world/blob/master/list_langs.py
#Only minor modifications were made.

import os
from urllib.parse import quote


readme = open('README.md', 'w')


# Copy template to README
with open('README_nolist.md', 'r') as temp:
  for line in temp:
    readme.write(line)

# Write title
readme.write('# Welcome\nThis repository is aimed to provide beginners with a starting point in their programming career. This project was inspired by [this GitHub repository](https://github.com/leachim6/hello-world). I thought that this would be a fun project to start, and my initial intentions were to do one language/day, but it\'s more sporatic than anything. Anyway, I hope you enjoy your stay, if there is anything I can do for you, feel free to sene me a message!\n ## This repository currently contains "Hello World" programs in the following conputer languages:\n')

# List the available languages
for dirname in sorted(os.listdir('.')):
  if not (dirname == '.' or dirname == '..' or dirname[0] == '.' or os.path.isfile(dirname)):
    subReadmeFN = os.path.join(dirname)+ '\\' + 'README.md'
    subReadme = open(subReadmeFN, 'w')
    for filename in sorted(os.listdir(dirname), key=lambda s: s.lower()):
      if not (filename == 'README.md'):
        if os.path.isfile(os.path.join(dirname, filename)):
          lang = os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()
          line = '* [{}]({})\n'.format(lang, quote(os.path.join(dirname, filename)))
          readme.write(line.replace('%5C', '/'))
        subReadme.write('* [{}]({})\n'.format(lang, quote(os.path.join(filename))))

readme.close()