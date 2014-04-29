#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Recalculate NOAA statistics for another climates.')

parser.add_argument('-i', '--inputfile', help='Input File.', required=True, type=argparse.FileType('r'))
parser.add_argument('-o', '--outputfile', help='Output File.', required=True, type=argparse.FileType('w'))
args=parser.parse_args()

print(args.inputfile)
print(args.outputfile)

