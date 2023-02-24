'''
Advent Of Code 2022.
https://adventofcode.com/2022/

This file is to run the selected challenge without manually opening the file
inside the folder. It also offers some useful flags lol.
'''

import argparse

def main():
    '''stuff'''        
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", dest="input", default=None, help="Input file location")
    parser.add_argument("-o", "--output", dest="output", default=None, help="Output file")
    
    args = parser.parse_args()
    val = []

    for line in open(args.input, mode='r', encoding="UTF-8").read().split('\n'):
        val.append(line)

    if args.output is not None:
        file_out = open(args.output, mode='w', encoding="UTF-8")
        for line in val:
            file_out.write(line + '\n')
    else:
        print(args.input, args.output, val)

if __name__ == "__main__":
    main()
