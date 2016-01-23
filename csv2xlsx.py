import os
import glob
import csv
from xlsxwriter.workbook import Workbook

"""
This scripts converts all csv files in INPUT_DIR to xlsx format.

Run the script using following command:

python csv2xlsx.py
"""
INPUT_DIR = 'inputs'

for csvfile in glob.glob(os.path.join(INPUT_DIR, '*.csv')):
    workbook = Workbook(csvfile.replace('.csv', '') + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()