#!/usr/bin/env python3
import csv
import os

# Замените 'folder_path' на путь к вашей директории с csv-файлами
folder_path = '/home/korobov/Change_csv_delimiter/ada-data'
delimiter = '|'
newDelimiter = '\t'

for folder in os.listdir(folder_path):
    if os.path.isdir(os.path.join(folder_path, folder)):
        for file in os.listdir(os.path.join(folder_path, folder)):
            if file.endswith('car_active.csv'):
                input_file = os.path.join(os.path.join(folder_path, folder), file)
                output_file = os.path.splitext(input_file)[0]+'_out.csv'
                print(input_file)
                with open(input_file,"r") as f_in, open(output_file,"w") as f_out:
                    reader = csv.reader(f_in, delimiter=delimiter, quotechar='"')
                    writer = csv.writer(f_out, delimiter=newDelimiter, quotechar='"')
                    for row in reader:
                        row_list = list(row)
                        writer.writerow(row_list)

