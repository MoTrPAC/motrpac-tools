#!/usr/bin/env python
"""
This script transforms CSV To Json,
returning a string representing a json object from a dict.

Usage: csvToJsonDumps.py <INFILE> <OUTFILE> <KEYCOL> [--help] [options]

Examples:
  csvToJsonDumps.py 'csvToJsonDumps_csv.csv' 'csvToJsonDumps_json.json' 'bid'

Arguments:
    INFILE        input CSV file
    OUTFILE       output JSON file
    KEYCOL        key column name from CSV file

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt  # pip install docopt==0.6.2
import csv
import json


class CsvToJsonDumps(object):
    def __init__(self, csv_infile, json_outfile, key_column):
        self.infile = csv_infile
        self.outfile = json_outfile
        self.keyColumn = key_column

    def transform_csv_to_json(self):
        data = {}
        with open(self.infile) as csvFile:
            csvReader = csv.DictReader(csvFile)

            for rows in csvReader:
                key = rows[self.keyColumn]
                data[key] = rows

        with open(self.outfile, 'w') as jsonFile:
            jsonFile.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    args = docopt(__doc__, version='CsvToJsonDumps 1.0')
    setup = CsvToJsonDumps(
        csv_infile=args['<INFILE>'], json_outfile=args['<OUTFILE>'], key_column=args['<KEYCOL>'])
    setup.transform_csv_to_json()
