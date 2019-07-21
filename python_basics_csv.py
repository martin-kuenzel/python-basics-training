#!/usr/bin/python3
import csv
import os

script_dir = os.path.realpath( os.path.dirname(__file__) )
testfiles_in = os.path.join(script_dir,'testfiles_input')
testfiles_out = os.path.join(script_dir,'testfiles_output')

with open(os.path.join(testfiles_in,'Example.csv')) as f:
    #csv_reader = csv.reader(f)
    csv_reader = csv.DictReader(f)
    with open(os.path.join(testfiles_out,'Example_out.csv'),mode='w') as f_out:
        # csv_writer = csv.writer(f_out,delimiter='|')
         
        # the fieldnames have to be supplied to the csv.DictWriter, but notice that we can easily remove fields here (more in at the beginning of the for loop for writing the output)
        csv_writer = csv.DictWriter(f_out, ['id','col1', 'col2'] )
        csv_writer.writeheader()
        for line in csv_reader:
            del line['col3'] # with DictWriter deleting whole columns from the output is easily possible
            csv_writer.writerow(line)
            print(f'{line} written to {f_out.name}')