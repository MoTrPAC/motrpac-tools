# motrpac-tools
Scripts and Tools useful for MoTrPAC


## hash_files.py

- Simple file to output hash digests for files
- Requires [Python 3.x](https://www.python.org)
- Examples:
    - `./hash_files.py --help`

       _outputs help info_

  - `./hash_files.py --algorithm md5 --ending pdf -recursive -output output.txt -verbose`

     _gets md5 hash for all files ending in `pdf` down a directory tree and writes the results to a file called `output.txt`_

  - `./hash_files.py --algorithm sha256 --file text.txt -verbose`

     _gets sha256 hash for the file `text.txt` in the current directory and outputs the results to the terminal only_

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
