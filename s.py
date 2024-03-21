import numpy as np
import matplotlib.pyplot as plt

def temperature_distribution(L, Pe, x):
    if Pe==0:
       return x
    else:
       return ((np.exp(Pe * x / L)) - 1) / (np.exp(Pe) - 1)

# Define parameters
L = 1.0  # Length of the domain (m)
Pe_values = [-100, -1.0, 0.0, 1.0, 100]  # Peclet numbers
x = np.linspace(0, L, 100)  # Discretized positions along the domain

# Plot the temperature distribution for each Peclet number
for Pe in Pe_values:
  T = temperature_distribution(L, Pe, x)
  plt.plot(x, T, label=f"Pe = {Pe}")

# Customize the plot
plt.xlabel("Length (m)")  # Corrected label for clarity
plt.ylabel("Temperature (T)")
plt.title("Temperature Distribution at Different Peclet Numbers")
plt.legend()
plt.grid(True)
plt.show()

