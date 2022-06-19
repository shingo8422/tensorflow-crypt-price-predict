import csv
import math

with open('../data/main.csv') as csv_file:
    spamreader = csv.reader(csv_file)
    rows = [row for row in spamreader]
    count = len(rows)
    with open('./data/ignore_volume.csv', 'w', newline='') as generated_csv_file:
        writer = csv.writer(generated_csv_file)
        data = []
        i = 0
        for row in rows:
            if i == (count - 5):
                break
            if i >= 100:
                line = [
                    row[0],
                ]
                for k in range(100):
                    line.append(math.floor((int(rows[i - k][2]) + int(rows[i - k][3])) / 2))
                line.append(math.floor((int(rows[i + 5][2]) + int(rows[i + 5][3])) / 2))
                data.append(line)
            i += 1
        writer.writerows(data)