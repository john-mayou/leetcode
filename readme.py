import os
import re
from textwrap import dedent

links = []
for dir in [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.')]:
  parts = dir.split('-')
  links.append(f'- [{parts[0]}. {' '.join(parts[1:]).title()}](./{dir})')

readme = dedent("""\
  This is a collection of Leetcode solutions with detailed explanations, including brute-force and optimal approaches, as well as time and space complexity analysis.
  
  These files are also viewable on my [personal website](https://johnmayou.com) and additional solutions can be found on my [Leetcode profile](https://leetcode.com/u/johnmayou/).
  
  List of problems:
  
  """)

with open('README.md', 'w') as f:
  f.write(readme + "\n".join(links))