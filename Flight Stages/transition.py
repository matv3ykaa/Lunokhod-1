import matplotlib.pyplot as plt

m = 273000
u1 = 9258
u2 = 543
r1 = 46738
r2 = 42164000
r = r2 / r1
I = 2796
g = 9.81

V1 = u1 * ((2 * r / (r + 1))**0.5 - 1)
V2 = u2 * (1 - (2 / (r + 1))**0.5)
P = 65500
e = (r2 - r1) / (r2 + r1)

t = [i for i in range(1, 213)]

fuel_values = list()
M = 2155
M1 = round(m * (1 - (e**(-((V1) / I)))))
M2 = round(m * (1 - (e**(-((V2) / I)))))
for i in range(1, abs(M1) + 1, 100):
    fuel_values.append(M - i)

curr_M = fuel_values[-1]

for r in range(200):
    fuel_values.append(curr_M)

for i in range(1, abs(M2) + 1, 50):
    fuel_values.append(curr_M - i)


print(fuel_values, M1, M2)
plt.plot(t, fuel_values)
plt.title('Зависимость количества топлива от времени')
plt.xlabel('Время, мин')
plt.ylabel('Количество топлива, кг')
plt.grid(True)
plt.yticks(plt.yticks()[0], [f'{int(y)}' for y in plt.yticks()[0]])
plt.show()
