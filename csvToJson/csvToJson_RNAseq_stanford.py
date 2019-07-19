"""
This script transforms CSV To Json.
An user needs to define the JSON format.

Usage: csvToJson_RNAseq.py <INFILE> <OUTFILE> <KEYCOL> [--help] [options]

Examples:
  csvToJson_RNAseq.py 'csvToJson_RNAseq_stanford.csv' 'csvToJson_RNAseq_stanford.json' 'vial_label'

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
                twoD_barcode = row["2D_barcode"]
                Species = row["Species"]
                BID = row["BID"]
                PID = row["PID"]
                Tissue = row["Tissue"]
                Sample_category = row["Sample_category"]
                GET_site = row["GET_site"]
                RNA_extr_plate_ID = row["RNA_extr_plate_ID"]
                RNA_extr_date = row["RNA_extr_date"]
                RNA_extr_conc = row["RNA_extr_conc (ng/uL)"]
                RIN = row["RIN"]
                r_260_280 = row["r_260_280"]
                r_260_230 = row["r_260_230"]
                Lib_prep_date = row["Lib_prep_date"]
                Lib_RNA_conc = row["Lib_RNA_conc (ng/ul)"]
                Lib_RNA_vol = row["Lib_RNA_vol (ul)"]
                Lib_robot = row["Lib_robot"]
                Lib_vendor = row["Lib_vendor"]
                Lib_type = row["Lib_type"]
                Lib_kit_id = row["Lib_kit_id"]
                Lib_batch_ID = row["Lib_batch_ID"]
                Lib_barcode_well = row["Lib_barcode_well"]
                Lib_index_1 = row["Lib_index_1"]
                Lib_index_2 = row["Lib_index_2"]
                Lib_adapter_1 = row["Lib_adapter_1"]
                Lib_adapter_2 = row["Lib_adapter_2"]
                Lib_UMI_cycle_num = row["Lib_UMI_cycle_num (bp)"]
                Lib_adapter_size = row["Lib_adapter_size (bp)"]
                Lib_frag_size = row["Lib_frag_size (bp)"]
                Lib_DNA_conc = row["Lib_DNA_conc (ng/uL)"]
                Lib_molarity = row["Lib_molarity (nM)"]
                Seq_platform = row["Seq_platform"]
                Seq_date = row["Seq_date"]
                Seq_machine_ID = row["Seq_machine_ID"]
                Seq_flowcell_ID = row["Seq_flowcell_ID"]
                Seq_flowcell_run = row["Seq_flowcell_run"]
                Seq_flowcell_lane = row["Seq_flowcell_lane"]
                Seq_flowcell_type = row["Seq_flowcell_type"]
                Seq_length = row["Seq_length"]
                Seq_end_type = row["Seq_end_type"]
                
                
                my_dict = {"@vial_label": vial_label,
                            "2D_barcode": twoD_barcode,
                            "Species": Species,
                            "BID": BID,
                            "PID": PID,
                            "Tissue": Tissue,
                            "Sample_category": Sample_category,
                            "GET_site": GET_site,
                            "RNA_extr_plate_ID": RNA_extr_plate_ID,
                            "RNA_extr_date": RNA_extr_date,
                            "RNA_extr_conc (ng/uL)": RNA_extr_conc,
                            "RIN": RIN,
                            "r_260_280": r_260_280,
                            "r_260_230": r_260_230,
                            "Lib_prep_date": Lib_prep_date,
                            "Lib_RNA_conc (ng/ul)": Lib_RNA_conc,
                            "Lib_RNA_vol (ul)": Lib_RNA_vol,
                            "Lib_robot": Lib_robot,
                            "Lib_vendor": Lib_vendor,
                            "Lib_type": Lib_type,
                            "Lib_kit_id": Lib_kit_id,
                            "Lib_batch_ID": Lib_batch_ID,
                            "Lib_barcode_well": Lib_barcode_well,
                            "Lib_index_1": Lib_index_1,
                            "Lib_index_2": Lib_index_2,
                            "Lib_adapter_1": Lib_adapter_1,
                            "Lib_adapter_2": Lib_adapter_2,
                            "Lib_UMI_cycle_num (bp)": Lib_UMI_cycle_num,
                            "Lib_adapter_size (bp)": Lib_adapter_size,
                            "Lib_frag_size (bp)": Lib_frag_size,
                            "Lib_DNA_conc (ng/uL)": Lib_DNA_conc,
                            "Lib_molarity (nM)": Lib_molarity,
                            "Seq_platform": Seq_platform,
                            "Seq_date": Seq_date,
                            "Seq_machine_ID": Seq_machine_ID,
                            "Seq_flowcell_ID": Seq_flowcell_ID,
                            "Seq_flowcell_run": Seq_flowcell_run,
                            "Seq_flowcell_lane": Seq_flowcell_lane,
                            "Seq_flowcell_type": Seq_flowcell_type,
                            "Seq_length": Seq_length,
                            "Seq_end_type": Seq_end_type
                            }
                my_list.append(my_dict)
        with open(self.outfile, 'w') as outfile:
            json.dump(my_list, outfile, indent=4)


if __name__ == '__main__':
    args = docopt(__doc__, version='CsvToJsonFormat 1.0')
    setup = CsvToJsonFormat(
        csv_infile=args['<INFILE>'], json_outfile=args['<OUTFILE>'], key_column=args['<KEYCOL>'])
    setup.transform_csv_to_json()
