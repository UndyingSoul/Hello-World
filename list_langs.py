#!/usr/bin/env python3
#Found here: https://github.com/leachim6/hello-world/blob/master/list_langs.py

import os
from urllib.parse import quote


readme = open('README.md', 'w')


# Copy template to README
with open('README_nolist.md', 'r') as temp:
  for line in temp:
    readme.write(line)

# Write title
readme.write('### This repository currently contains "Hello World" programs in the following languages:\n')

# List the available languages
for dirname in sorted(os.listdir('.')):
  if not (dirname == '.' or dirname == '..' or dirname[0] == '.' or os.path.isfile(dirname)):
    for filename in sorted(os.listdir(dirname), key=lambda s: s.lower()):
      if not (filename == 'README.md'):
        if os.path.isfile(os.path.join(dirname, filename)):
          lang = os.path.splitext(filename)[0].replace('-', ' ').replace('_', ' ').title()
          readme.write('* [{}]({})\n'.format(lang, quote(os.path.join(dirname, filename))))
        subReadmeFN = os.path.join(dirname)+ '\\' + 'README.md'
        subReadme = open(subReadmeFN, 'w')
        subReadme.write('* [{}]({})\n'.format(lang, quote(os.path.join(filename))))

readme.close()