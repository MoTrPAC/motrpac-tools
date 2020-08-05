# motrpac-tools
Scripts and Tools useful for MoTrPAC

## make_manifest.py

- Simple file to show how to make has digests. THIS DOES NOT MATCH THE CURRENT SPEC
- Requires [Python 3.x](https://www.python.org)
- Examples:
    - `./make_manifest.py --help`

       _outputs help info_


  - `./python make_manifest.py /path/to/upload/ manifest.csv`

     _makes manifest.cvs based on files in /path/to/upload/_

```
usage: make_manifest.py [-h] data_path output

Creates manifest for submission to BIC: a comma separated file table of
relative file paths and md5 sums.

positional arguments:
  data_path   full base path of the data submission
  output      path to the output file

optional arguments:
  -h, --help  show this help message and exit
```


## hash_files.py

- Simple file to show how to make has digests. THIS DOES NOT MATCH THE CURRENT SPEC
- Requires [Python 3.x](https://www.python.org)
- Examples:
    - `./hash_files.py --help`

       _outputs help info_

  - `./hash_files.py --algorithm md5 --ending pdf --recursive --output output.txt --verbose`

     _gets md5 hash for all files ending in `pdf` down a directory tree and writes the results to a file called `output.txt`_

  - `./hash_files.py --algorithm sha256 --file text.txt --verbose`

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
