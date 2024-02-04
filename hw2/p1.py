import numpy as np
<<<<<<< HEAD
import matplotlib.pyplot as plt

def union_func(x,y):
    return (x ** 2) * (y) - (2 * x)

x_vals = np.linspace(0,1,0.01)
y_vals = np.linspace(0,1,0.01)

x_mesh, y_mesh = np.meshgrid(x_values, y_values)

output = union_func(x_mesh, y_mesh)

plt.contourf(x_mesh, y_mesh, output, cmap='viridis')

plt.show()
=======
import matplotlib
matplotlib.use('TkAgg')  # Use 'Agg' backend
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(0.001, 10, 100)

# Defining The Function
def funcLower(x):
    return ((2 * x) ** -1) - (x ** -2)

def funcHigher(x):
    return 2 * (x ** -1)

# Calculate corresponding y values
y1_values = funcLower(x_values)
y2_values = funcHigher(x_values)

# Plot the function
plt.plot(x_values, y1_values, label = "Bounds")
plt.plot(x_values, y2_values, label = "Bounds")

# Bounds
plt.axhline(1, color = 'blue', linestyle = '--', label = 'y = 1')
plt.axhline(0, color = 'blue', linestyle = '--', label = 'y = 0')
plt.axvline(1, color = 'red', linestyle = '--', label = 'x = 1')
plt.axvline(0, color = 'red', linestyle = '--', label = 'x = 0')

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Problem One Plot')

# Save the plot as a PNG file
plt.show()
plt.savefig('p1.png')

>>>>>>> d5e88abbb613e7ab1a0aa6b3c55378da3059625f
