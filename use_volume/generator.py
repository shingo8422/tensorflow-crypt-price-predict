import csv
import math

with open('../data/main.csv') as csv_file:
    spamreader = csv.reader(csv_file)
    rows = [row for row in spamreader]
    count = len(rows)
    with open('./data/use_volume.csv', 'w', newline='') as generated_csv_file:
        writer = csv.writer(generated_csv_file)
        data = []
        i = 0
        for row in rows:
            if i == (count - 5):
                break
            if i >= 120:
                line = [
                    row[0],
                ]
                for k in range(120):
                    line.append(int(rows[i - k][1]))
                    line.append(int(rows[i - k][2]))
                    line.append(int(rows[i - k][3]))
                    line.append(int(rows[i - k][4]))
                    line.append(float(rows[i - k][5]))
                line.append(int(rows[i + 5][2]))
                data.append(line)
            i += 1
        writer.writerows(data)