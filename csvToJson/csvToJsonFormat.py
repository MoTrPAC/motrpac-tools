"""
This script transforms CSV To Json.
An user needs to define the JSON format.

Usage: csvToJsonFormat.py <INFILE> <OUTFILE> <KEYCOL> [--help] [options]

Examples:
  csvToJsonFormat.py 'csvToJsonFormat_csv.csv' 'csvToJsonFormat_json.json' 'vial_label'

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
import datetime


class CsvToJsonFormat(object):
    def __init__(self, csv_infile, json_outfile, key_column):
        self.infile = csv_infile
        self.outfile = json_outfile
        self.keyColumn = key_column

    def transform_csv_to_json(self):
        my_list = []
        with open(self.infile) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vial_label = int(row[self.keyColumn])
                species = row["species"]
                ext_date = row["ext_date"]
                Lib_DNA_conc = float(row["Lib_DNA_conc (ng/uL)"])
                my_dict = {"@vial_label": vial_label,
                           "species": species,
                           "ext_date": ext_date,
                           "Lib_DNA_conc": Lib_DNA_conc}
                my_list.append(my_dict)
        with open(self.outfile, 'w') as outfile:
            json.dump(my_list, outfile, indent=4)


if __name__ == '__main__':
    args = docopt(__doc__, version='CsvToJsonFormat 1.0')
    setup = CsvToJsonFormat(
        csv_infile=args['<INFILE>'], json_outfile=args['<OUTFILE>'], key_column=args['<KEYCOL>'])
    setup.transform_csv_to_json()
