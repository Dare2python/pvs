import numpy as np


#  https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/
#  numpy.random.normal.html
#  https://en.wikipedia.org/wiki/Gaussian_function
#  https://en.wikipedia.org/wiki/Normal_distribution
def makeGaussian(mu=14, step=1, sigma=3):
    """ Make gaussian.
    mu is the mean value
    step is an interval for dot plotting
    sigma is the standard deviation.
    """

    x = np.arange(mu - 3*sigma, mu + 3*sigma, step, float)

    y = 1/(sigma * np.sqrt(2 * np.pi)) \
        * np.exp(- (x - mu)**2 / (2 * sigma**2))

    return x, y
