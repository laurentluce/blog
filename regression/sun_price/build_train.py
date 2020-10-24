import collections

import csv

counties = dict()
with open('sun_hours.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        try:
            county_id, hours = row[0], int(row[1])
            counties[county_id] = [hours]
        except ValueError:
            pass

prices = collections.defaultdict(list)
with open('price.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        try:
            county_id, price = row[1][:2], float(row[10])
            prices[county_id].append(price)
        except ValueError:
            pass

prices = {k:sum(v) / len(v) for (k, v) in prices.items()}

for k, v in counties.items():
    if k in prices:
        v.append(prices[k])

counties = {k:v for (k, v) in counties.items() if len(v) == 2}

with open('train.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    for k, v in counties.items():
        writer.writerow([k, v[0], v[1]])