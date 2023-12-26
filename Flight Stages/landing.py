import matplotlib.pyplot as plt

m0 = 58000
m = 1208
P = 68000
U = 1400
g = 1.63
k = 330

t = [i for i in range(1, 18, 2)]
t1 = [1, 30, 60, 90, 120, 150, 180, 210, 240]

fuel_values = list()

for i in range(len(t)):
    wy = P / (m0 - k * t[i])
    V =  U - wy * t[i]
    M = m - P / (V / t[i] - g)
    fuel_values.append(M)


plt.plot(t1, fuel_values)
plt.title('Зависимость количества топлива от времени')
plt.xlabel('Время, сек')
plt.ylabel('Количество топлива, кг')
plt.grid(True)
plt.show()
