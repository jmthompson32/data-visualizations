import matplotlib.pyplot as plt
from matplotlib import colormaps

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.plasma, s=10)

ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cube of Value", fontsize=12)

plt.show()
