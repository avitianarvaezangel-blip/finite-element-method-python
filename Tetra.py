import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


V = np.array([
    [1, 1, 2],  
    [0, 0, 0],  
    [0, 2, 0], 
    [2, 1, 0] 
])

i = V[0,:]

print(i)


caras = [
    [V[0], V[1], V[2]],
    [V[0], V[1], V[3]],
    [V[1], V[2], V[3]],
    [V[2], V[0], V[3]]
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.add_collection3d(Poly3DCollection(caras, alpha=0.5, edgecolor='b'))


ax.scatter(V[:,0], V[:,1], V[:,2], color='b')


ax.set_xlim([0,2])
ax.set_ylim([0,2])
ax.set_zlim([0,2])


plt.xlabel("x")

plt.ylabel("y")


plt.show()
