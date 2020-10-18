import csv

towns = dict()

with open('population.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        try:
            town_code, unemployed, active = row[0], float(row[22]), float(row[23])
            unemployment = unemployed / active * 100
            towns[town_code] = [unemployment]
        except (ValueError, ZeroDivisionError):
            pass

with open('price.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        town_code, price = row[1], row[10]
        if town_code in towns:
            try:
                towns[town_code].append(float(price))
            except ValueError:
                pass

towns = {k:v for (k, v) in towns.items() if len(v) == 2}

with open('train.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    for k, v in towns.items():
        writer.writerow([k, v[0], v[1]])


