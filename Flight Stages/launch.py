import matplotlib.pyplot as plt

m_r = 260093
m0 = 276093
m = 16000
P1 = 996000
P2 = 325000
P3 = 62500
U = 9285

t = [i for i in range(1, 336, 10)]
t1 = [i for i in range(1, 111, 10)]
t2 = [i for i in range(1, 113,10)]
t3 = [i for i in range(1, 111,10)]

g = 9.81
Cx = 0.018
rho = 0.125
Se = 20.1
k1 = 110
k2 = 110
k3 = 110 

fuel_values = list()

for i in range(len(t1)):
    wy = P1 / (m0 - k1 * t1[i])
    V = wy * t1[i]
    Fc = (Cx * rho * Se * V**2) / 2
    M = m - (P1 - Fc) / (U / t1[i] + g)
    fuel_values.append(M)

m = M
m0 = m_r + fuel_values[-1]

for i in range(len(t2)):
    wy = P2 / (m0 - k2 * t2[i])
    V = wy * t2[i]
    Fc = (Cx * rho * Se * V**2) / 2
    M = m - (P2 - Fc) / (U / t2[i] + g)
    fuel_values.append(M)

m = M
m0 = m_r + fuel_values[-1]

for i in range(len(t3)):
    wy = P3 / (m0 - k3 * t3[i])
    V = wy * t3[i]
    Fc = (Cx * rho * Se * V**2) / 2
    M = m - (P3 - Fc) / (U / t3[i] + g)
    fuel_values.append(M)

plt.plot(t, fuel_values)
plt.title('Зависимость количества топлива от времени')
plt.xlabel('Время, сек')
plt.ylabel('Количество топлива, кг')
plt.grid(True)
plt.yticks(plt.yticks()[0], [f'{int(y)}' for y in plt.yticks()[0]])
plt.show()
