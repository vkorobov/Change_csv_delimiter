#!/usr/bin/env python3
import csv
import sys, getopt
import os

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "hi:o:d:n:"
 
# Long options
long_options = ["Help", "Input=", "Output=", "Delimiter=", "NewDelimiter="]
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for opt, arg in arguments:
 
        if opt in ("-h", "--Help"):
            print ("Usage -i inputfile.csv -o outputfile.csv -d 'delimiter' -n 'new delimiter'")
            exit(1)
             
        elif opt in ("-i", "--Input"):
            # print (("Input file (% s)") % (arg))
            input_file = arg
            # print(os.path.splitext(input_file)[0])    
            output_file = os.path.splitext(input_file)[0]+'_out.csv'
            # print(output_file)

        elif opt in ("-o", "--Output"):
            # print (("Outputfile (% s)") % (arg))
            output_file = arg

        elif opt in ("-d", "--Delimiter"):
            # print (("Delimiter (% s)") % (arg))
            delimiter = arg

        elif opt in ("-n", "--NewDelimiter"):
            # print (("New Delimiter (% s)") % (arg))
            newDelimiter = arg
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))


# Bug: escaped symbols not parsed from arguments.
# Temporary replace newdelimiter to tab in code.
newDelimiter = '\t'

with open(input_file,"r") as f_in, open(output_file,"w") as f_out:
    reader = csv.reader(f_in, delimiter=delimiter, quotechar='"')
    writer = csv.writer(f_out, delimiter=newDelimiter, quotechar='"')
    for row in reader:
        # row_string = '\t'.join(row)
        # print(row_string)
        row_list = list(row)
        # for i in range(len(row_list)):
        #     if row_list[i] == '|':
        #         row_list[i] = '\t'
        # row_string = '+'.join(row_list)
        # print(row_string)

        writer.writerow(row_list)

