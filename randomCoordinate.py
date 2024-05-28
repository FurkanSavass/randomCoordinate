import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


num_points = 1000
x_coords = np.random.randint(0, 1001, num_points)
y_coords = np.random.randint(0, 1001, num_points)


data = {'X': x_coords, 'Y': y_coords}
df = pd.DataFrame(data)


df.to_excel('/mnt/data/koordinatlar.xlsx', index=False)


df = pd.read_excel('/mnt/data/koordinatlar.xlsx')


grid_size = 200


df['GridX'] = df['X'] // grid_size
df['GridY'] = df['Y'] // grid_size
df['Color'] = df['GridX'] + df['GridY'] * (1000 // grid_size)


fig, ax = plt.subplots(figsize=(10, 10))
scatter = ax.scatter(df['X'], df['Y'], c=df['Color'], cmap='tab20', alpha=0.6)


plt.colorbar(scatter, ax=ax)


ax.set_xticks(np.arange(0, 1001, grid_size))
ax.set_yticks(np.arange(0, 1001, grid_size))
ax.grid(which='both')

plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.title('Rastgele Noktaların 200x200 Izgarada Görselleştirilmesi')
plt.show()
