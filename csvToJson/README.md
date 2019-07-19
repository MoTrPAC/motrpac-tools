# Scripts to transform CSV to JSON
- All the following three scripts transform CSV to JSON. Each file has different configurations.
- Requires [Python 3.x](https://www.python.org)
- Json schema such as header names and data type needs to be defined for your own CSV format. Current scripts are hard-coded to fit the example CSV files (csvToJsonFormat_csv.csv, csvToJson_RNAseq_stanford.csv)

## csvToJsonDumps.py
``` 
Usage:
csvToJsonDumps.py <INFILE> <OUTFILE> <KEYCOL> [--help]  [options]

Examples:
csvToJsonDumps.py 'csvToJsonDumps_csv.csv' 'csvToJsonDumps_json.json' 'bid'

Arguments:
INFILE input CSV file
OUTFILE output JSON file
KEYCOL key column name from CSV file

Options:
-h --help Show this screen.
--version Show version.
```

## csvToJsonFormat.py

```
Usage: 
csvToJsonFormat.py <INFILE> <OUTFILE> <KEYCOL> [--help]  [options]

Examples:
csvToJsonFormat.py 'csvToJsonFormat_csv.csv' 'csvToJsonFormat_json.json' 'vial_label'

Arguments:

INFILE input CSV file
OUTFILE output JSON file
KEYCOL key column name from CSV file

Options:
-h --help Show this screen.
--version Show version.
```

## csvToJson_RNAseq_stanford.py

```
Usage: 
csvToJson_RNAseq.py <INFILE> <OUTFILE> <KEYCOL> [--help]  [options]

Examples:
csvToJson_RNAseq.py 'csvToJson_RNAseq_stanford.csv' 'csvToJson_RNAseq_stanford.json' 'vial_label'

Arguments:
INFILE input CSV file
OUTFILE output JSON file
KEYCOL key column name from CSV file

Options:
-h --help Show this screen.
--version Show version.
```