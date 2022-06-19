import csv
import math

with open('./data/ignore_volume.csv') as csv_file:
    spamreader = csv.reader(csv_file)
    rows = [row for row in spamreader]
    count = len(rows)

    print(rows[0])
    print(len(rows[0]))
    print(count)