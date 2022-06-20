import csv
import math

data_price_before_minutes = 120
target_price_after_minutes = 5

with open('../data/main.csv') as csv_file:
    spamreader = csv.reader(csv_file)
    rows = [row for row in spamreader]
    count = len(rows)
    with open('./data/use_volume.csv', 'w', newline='') as generated_csv_file:
        writer = csv.writer(generated_csv_file)
        data = []
        i = 0
        for row in rows:
            if i == (count - target_price_after_minutes):
                break
            if i >= data_price_before_minutes:
                line = [
                    row[0],
                ]
                for k in range(data_price_before_minutes):
                    line.append(int(rows[i - k][1]))
                    line.append(int(rows[i - k][2]))
                    line.append(int(rows[i - k][3]))
                    line.append(int(rows[i - k][4]))
                    line.append(float(rows[i - k][5]))
                line.append(math.floor((int(rows[i + target_price_after_minutes][2]) + int(rows[i + target_price_after_minutes][3])) / 2))
                data.append(line)
            i += 1
        writer.writerows(data)