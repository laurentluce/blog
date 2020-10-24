import csv
import numpy as np
from sklearn.linear_model import LinearRegression

towns = dict()

x, y = [], []

with open('train.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        sun_hours, price = float(row[1]), float(row[2])
        x.append(sun_hours)
        y.append(price)

x = np.array(x).reshape((-1, 1))
y = np.array(y)

model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
print(r_sq)
print(model.intercept_)
print(model.coef_)

# x_new = np.array([8, 10, 12, 14, 16]).reshape((-1, 1))
# y_new = model.predict(x_new)
# print(y_new)