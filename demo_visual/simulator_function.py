import numpy as np


#  https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/
#  numpy.random.normal.html
#  https://docs.scipy.org/doc/scipy/reference/generated/
#  scipy.stats.norm.html
#  https://en.wikipedia.org/wiki/Gaussian_function
#  https://en.wikipedia.org/wiki/Normal_distribution
def makeGaussian(mu=14, step=0.3, sigma=3, max_value=3.3):
    """ Make gaussian.
    mu is the mean value
    step is an interval for dot plotting
    sigma is the standard deviation.
    """

    # hstack approach for combining ndarrays

    # 0 - 4:30 zeroes
    x1 = np.arange(0, 4.5, step, float)
    y1 = 0 * x1

    # 4:30 - 8:00 line
    x2 = np.arange(4.5, 8, step, float)
    # f(4:30) == 0
    # f(8:00) == 400
    y2 = 50 * (x2-4.5)

    # 8:00-20:00 Gaussian
    x3 = np.arange(8, 20, step, float)
    y3 = max_value * 1/(sigma * np.sqrt(2 * np.pi)*0.1336) \
        * np.exp(- (x3 - mu)**2 / (2 * sigma**2))

    # 20:00-21:00 line
    x4 = np.arange(20, 21, step, float)
    # f(20) == 100
    # f(21) == 0
    y4 = 100 - 5 * (x4-20)

    # 21:00-24 zeroes
    x5 = np.arange(21, 24, step, float)
    y5 = 0 * x5

    return np.hstack((x1,x2, x3, x4, x5)), np.hstack((y1, y2, y3, y4, y5))

    # x = np.arange(0, 24, step, float)
    # y = max_value - 70 * (mu - x * 1.0574) ** 2

    # f(8 a.m./8:00) == 400 (=check8)
    # f(8 p.m./20:00)== 100 (=check20)

# two ways to create complex function
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfunction.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.hstack.html?highlight=hstack#numpy.hstack
