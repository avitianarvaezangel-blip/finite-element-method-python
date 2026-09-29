import numpy as np
import matplotlib.pyplot as plt

import math as m

# nodos
i = np.array([0, -1])
j = np.array([2, 0])
k = np.array([0, 1])

# Vector desplazamientos
u = np.array([0, 2.5e-3, 1.2e-3, 0, 0, 2.5e-3])

U = u.reshape(-1, 1)

A = 2

print("u = ",U)

E = 30e6
t = 1
v = 0.25

# Mariz de Deformacion

b = 1/(2*A)

# b's

bi = j[1] - k[1]

bj = k[1] - i[1]

bk = i[1] - j[1]

# c's

ci = k[0] - j[0]

cj = i[0] - k[0]

ck = j[0] - i[0]

B = b* np.array([[bi, 0, bj, 0,bk, 0],[0, ci, 0, cj, 0, ck],[ci, bi, cj, bj, ck, bk]])

Bt = np.transpose(B)

print("Bt =",Bt)

# Mtriz Constitutiva

d = (E)/(1 - v**2)

D = d * np.array([[1, v, 0],[v, 1, 0],[0, 0, (1 - v)/2]])

print("D =",D)

# Esfuerzo

sigma = (D@B)@U

print("sigma =", sigma)


K = (A*t)*Bt@D@B

print("K = ",K)

s_max = (sigma[0,0] + sigma[1,0])/2 + m.sqrt(((sigma[0,0] - sigma[1,0])/2 )**2 + sigma[2,0]**2)

s_min = (sigma[0,0] + sigma[1,0])/2 - m.sqrt(((sigma[0,0] - sigma[1,0])/2 )**2 + sigma[2,0]**2)

print("s_max =",s_max)

print("s_min =",s_min)


# original


x = [i[0], j[0], k[0], i[0]]


y = [i[1], j[1], k[1], i[1]]


plt.plot(x, y, marker='o', color='b')

plt.fill(x, y, alpha=0.3, color='b',)

# despues de la demormacion


x2 = [i[0] + 100*u[0], j[0] + 100*u[2], k[0] + 100*u[4], i[0] + 100*u[0]]

y2 = [i[1] + 100*u[1], j[1] + 100*u[3], k[1] + 100*u[5], i[1] + 100*u[1]]


plt.fill(x2, y2, alpha=0.3, color='r')


plt.plot(x2, y2, marker='o', color='r')

plt.axhline(0, color='k', alpha=0.5)

plt.axvline(0, color='k', alpha=0.5)


plt.title("Elemento Triangular")


plt.grid()





