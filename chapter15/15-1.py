from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

plt.scatter(x_values, cubes, edgecolor='none', s=40)

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()