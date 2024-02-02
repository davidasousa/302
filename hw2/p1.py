import numpy as np
import matplotlib.pyplot as plt

def union_func(x,y):
    return (x ** 2) * (y) - (2 * x)

x_vals = np.linspace(0,1,0.01)
y_vals = np.linspace(0,1,0.01)

x_mesh, y_mesh = np.meshgrid(x_values, y_values)

output = union_func(x_mesh, y_mesh)

plt.contourf(x_mesh, y_mesh, output, cmap='viridis')

plt.show()
