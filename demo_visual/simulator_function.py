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

    #x = np.arange(0, 24, step, float)
    #y = max_value * 1/(sigma * np.sqrt(2 * np.pi)*0.13) \
    #    * np.exp(- (x - mu)**2 / (2 * sigma**2))

    # hstack approach for combining
    x = np.arange(0, 24, step, float)
    y = max_value - (mu - x) ** 2

    # f(8 a.m.) == 400 (=check8)

    return x, y

# two ways to create complex function
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfunction.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.hstack.html?highlight=hstack#numpy.hstack
