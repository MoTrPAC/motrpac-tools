import hashlib
import os
import argparse


def MoTrPACManifest(basepath, outfile, sep=','):
    lines = 0
    o = open(outfile, 'w')
    o.write("file_name%smd5\n" % sep)
    for path, dirnames, filenames in os.walk(basepath):
        for fn in filenames:
            fp = os.path.join(path, fn)
            hasher = hashlib.md5()
            with open(str(fp), 'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
                afile.close()
            o.write(sep.join([fp.replace(basepath, ""),
                              hasher.hexdigest()])+"\n")
            lines += 1
    o.close()
    if lines == 0:
        raise Exception("No files in basepath or basepath not found. "
                        "Please double check")
    else:
        print("wrote data for %d files" % lines)


def main():
    description = 'Creates manifest for submission to BIC: a comma ' \
                  'separated file table of relative file paths and md5 sums.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('data_path',
                        help='Full path to folder containing all files '
                             'for data submission')
    parser.add_argument('output', default='manifest.txt',
                        help='Path to the output file')
    args = parser.parse_args()
    MoTrPACManifest(args.data_path, args.output)


if __name__ == "__main__":
    main()
