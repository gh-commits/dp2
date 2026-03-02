import sys

fp = sys.argv[1]

with open(fp, 'r') as file:
    for line in file:
        print(line)
