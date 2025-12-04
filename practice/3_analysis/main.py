import numpy as np
from sklearn.linear_model import LinearRegression

# Допустим у тебя есть массивы времени и температуры
time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
temp = np.array([22, 23, 24, 23.5, 24.2, 24.8, 24.8, 24.8, 100])

model = LinearRegression()
model.fit(time, temp)

next_time = np.array([[len(time)+1]])
pred = model.predict(next_time)

print(pred[0])
