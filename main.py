__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'


import sys


fname = sys.argv[1]

with open(fname) as f:
    txt=f.read()

def count_char(txt, char):
    count = 0
    for c in txt:
        if c == char:
          count += 1
    return count


print("{0:^30}".format(f"Analysis of {fname}"))

for char in "abcdefghijklmnopqrstuvwxyz":
    perc=100*(count_char(txt,char)/len(txt))
    print("{0} - {1}%".format(char,round(perc,2)))
