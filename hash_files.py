#!/usr/bin/env python
import hashlib
import argparse
import glob

# note: docopt would be preferable but argparse
# is used here for portability (no imports required
# as it is part of the Python standard library)

# preferred algorithm support may change later
algorithm_choices = ['md5', 'sha512', 'sha256', 'sha1', 'sha3_512']
# check that each algorithm_choices is indeed available
# in hashlib (dependent upon the OpenSSL library that
# Python uses on the user's platform)
choices_algorithms_guaranteed = list(
                                hashlib.algorithms_guaranteed.
                                intersection(set(algorithm_choices)))

description = "Basic Hashing Tool Using Python's hashlib"
parser = argparse.ArgumentParser(usage=None, description=description)

parser.add_argument('-a', '--algorithm',
                    choices=choices_algorithms_guaranteed,
                    required=True,
                    help='algorithm to use')
parser.add_argument('-o', '--output',
                    const='hashing_output.txt',
                    nargs='?',
                    help='output file')
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='verbose')
parser.add_argument('-r', '--recursive',
                    action='store_true',
                    help='recursive down directories, when using --ending')

exgroup = parser.add_argument_group(
            title='choose one option: Hash a single file OR Hash many files')
group = exgroup.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--file',
                   help='file to hash')
group.add_argument('-e', '--ending',
                   help='hash files ending with suffix, e.g. txt')

args = parser.parse_args()

if args.verbose is True:
    print('Variables:\n----------------------')
    print('algorithm: ', args.algorithm)
    print('file[s] to hash: ' + (
        args.file if args.file else ('*.' + args.ending)))
    print('\n\nFile,  Hash(hexdigest)\n----------------------')

if args.output is not None:
    print('output file: ', args.output)
    output_file = open(args.output, 'a+')

files = glob.glob('**/*' + args.ending,
                  recursive=args.recursive) if args.ending else [args.file]


hasher_string = 'hashlib.' + args.algorithm
hasher = eval(hasher_string + '()')

# create hash digests for file[s]
for file in files:
    with open(file, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)

    output_string = file + ', ' + hasher.hexdigest()

    # output to terminal
    if args.verbose is True:
        print(output_string)

    # output to file
    if args.output:
        output_text = output_string + '\n'
        output_file.write(output_text)

if args.output:
    output_file.close()
