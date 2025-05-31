import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the CSV data using pandas
csv_file = 'SourceData_Fig2/112_geophysical_sections.csv'

df = pd.read_csv(csv_file)
df2 =pd.read_csv('SourceData_Fig2/112_location.csv')

# Extract x, y, and value columns
x = df['x'].values
y = df['z'].values*-1
values = df['Serp_Degree'].values

# Create a grid
x_unique = np.unique(x)
y_unique = np.unique(y)
X, Y = np.meshgrid(x_unique, y_unique)

# Initialize an empty grid for the values
Z = np.empty(X.shape)
Z[:] = np.nan  # Fill with NaN values initially

# Populate the grid with the values from the CSV
for i in range(len(x)):
    x_index = np.where(x_unique == x[i])[0][0]
    y_index = np.where(y_unique == y[i])[0][0]
    Z[y_index, x_index] = values[i]

# Create the heatmap using imshow
plt.figure(figsize=(16, 6))
plt.imshow(Z, cmap ='summer_r',extent=[x_unique.min(), x_unique.max(), y_unique.min(), y_unique.max()], origin='lower', aspect='auto')
plt.colorbar(label='Degree of Serpentinization')  # Add a colorbar to show the value scale
plt.plot(df2['x'],df2['bathymetry']*-1, color='black', linewidth=2, label='Bathymetry')  # Plot the bathymetry line
# Set labels and title
plt.xlabel('Distance (km)')
plt.ylabel('Depth (km)')
plt.title('Image from CSV Data')

# Show the plot
plt.show()
