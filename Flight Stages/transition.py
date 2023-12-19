import matplotlib.pyplot as plt

m = 2155
u2 = 2630
u1 = 1400
r1 = 4700000
r2 = 42164000
r = r2 / r1

V1 = u1 * (1 - (2 / (r + 1))**0.5)
V2 = u2 * (((2 * r) / (r + 1))**0.5 - 1)
P = 65500

t1 = [i for i in range(1, 11, 5)]
t2 = [i for i in range(1, 11, 5)]
t = [i for i in range(1, 36, 5)]

fuel_values = list()

for i in range(len(t1)):
    M = m - ((P * t1[i]) / V1)
    fuel_values.append(M)

m = M

for r in range(3):
  fuel_values.append(M)

for i in range(len(t2)):
    M = m - ((P * t2[i]) / V2)
    fuel_values.append(M)

plt.plot(t, fuel_values)
plt.title('Зависимость количества топлива от времени')
plt.xlabel('Время, сек')
plt.ylabel('Количество топлива, кг')
plt.grid(True)
plt.yticks(plt.yticks()[0], [f'{int(y)}' for y in plt.yticks()[0]])
plt.show()
