import random
import csv

with open ('list.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    rownum = len(list(csv_file))
    print(rownum)


    next(csv_file)
    for line in csv_reader:
        print(line)
