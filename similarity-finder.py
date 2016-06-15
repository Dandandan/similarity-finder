import difflib
import sys
from os import listdir
from os.path import isfile, join
import math

def main(file_names):
    if len(file_names) < 2:
        print('no files to compare')
    file_contents = [open(f).readlines() for f in file_names]
    num_files = len(file_names)
    sims = []
    for x in range(0, num_files):
        for y in range(x+1, num_files):
            s = difflib.SequenceMatcher(None, file_contents[x], file_contents[y])
            ratio = s.ratio()
            sims.append((file_names[x], file_names[y], ratio))

    sorted_sims = sorted(sims, key=lambda s: -s[2])

    for f1, f2, score in sorted_sims:
        print(f1 + ',' + f2 + ',' + str(score))

if __name__ == '__main__':
   path = sys.argv[1]
   file_names = [f for f in listdir(path) if isfile(join(path, f))]
   main(file_names)
