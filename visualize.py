# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
import simulator_function as f

# setting the x - coordinates
x = np.arange(0, 2 * np.pi, 0.1)
# setting the corresponding y - coordinates
y = f.function(x)

# potting the points
plt.plot(x, y)

# function to show the plot
plt.show()

