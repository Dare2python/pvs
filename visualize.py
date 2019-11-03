# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
import simulator_function as f

# setting the x - coordinates
mu = 14
step = 0.1
sigma = 3

# setting the corresponding y - coordinates
function = f.makeGaussian(mu, step, sigma)

# potting the points
plt.plot(*function)

# function to show the plot
plt.show()

