# motrpac-tools
Scripts and Tools useful for MoTrPAC


## hash_files.py

- Simple file to output hash digests for files
- Requires [Python 3.x](https://www.python.org)

```
usage: hash_files.py [-h] -a {sha256,sha3_512,sha1,sha512,md5} [-o [OUTPUT]]
                     [-v] [-r] (-f FILE | -e ENDING)

Basic Hashing Tool Using Python's hashlib

optional arguments:
  -h, --help            show this help message and exit
  -a {sha256,sha3_512,sha1,sha512,md5}, --algorithm {sha256,sha3_512,sha1,sha512,md5}
                        algorithm to use
  -o [OUTPUT], --output [OUTPUT]
                        output file
  -v, --verbose         verbose
  -r, --recursive       recursive down directories, when using --ending

choose one option: Hash a single file OR Hash many files:
  -f FILE, --file FILE  file to hash
  -e ENDING, --ending ENDING
                        hash files ending with suffix, e.g. txt
```
