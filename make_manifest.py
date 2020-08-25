import hashlib
import os
import argparse


def MoTrPACManifest(basepath, outfile, quiet=False, sep=','):
    BLOCKSIZE = 65536

    # Determine full paths
    outfilepath_full = os.path.abspath(outfile)
    basepath_full = os.path.abspath(basepath)
    basepath_full_length = len(basepath_full)
    
    lines = 0
    o = open(outfile, 'w')
    o.write("file_name%smd5\n" % sep)
    for path, dirnames, filenames in os.walk(basepath):
        for fn in filenames:
            fp = os.path.join(path, fn)
            
            filepath_full = os.path.abspath(fp)
            if outfilepath_full == filepath_full:
                # Do not hash the output file
                continue

            relativepath = filepath_full[basepath_full_length:].lstrip(os.path.sep)
            
            # Change path separators to / if running on Windows
            if os.path.sep != '/':
                relativepath = relativepath.replace(os.path.sep, '/')
                
            if not quiet:
                print(relativepath)

            hasher = hashlib.md5()
            with open(str(fp), 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)            
                afile.close()
                           
            o.write(sep.join([relativepath, hasher.hexdigest()]) + "\n")
            lines += 1
    o.close()
    if lines == 0:
        raise Exception("No files in basepath or basepath not found. "
                        "Please double check")
    else:
        print("wrote data for %d files" % lines)


def main():
    description = 'Creates manifest for submission to BIC: a comma ' \
                  'separated file with relative file paths and md5 sums.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('data_path',
                        help='Full path to folder containing all files '
                             'for data submission')
    parser.add_argument('output', default='file_manifest.csv',
                        help='Path to the output file')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='When provided, do not show file paths as they are hashed.')
    args = parser.parse_args()
    MoTrPACManifest(args.data_path, args.output, args.quiet)


if __name__ == "__main__":
    main()
