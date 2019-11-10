# importing the required modules
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from demo_visual import simulator_function as f

# setting the x - coordinates
mu = 14
step = 0.3
sigma = 3
max_value = 3300  # kW power

# setting the corresponding y - coordinates
function = f.makeGaussian(mu, step, sigma, max_value)

x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)

# potting the points
plt.plot(*function)
# plt.plot(x, norm.pdf(x, 14, sigma))

# function to show the plot
plt.show()

