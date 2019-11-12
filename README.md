# PV Simulator

## Task
To build an application which generates simulated PV (photovoltaic) power values (in kW)

### Simulator function approximation
The picture of a real PV power output curve during a normal day is given as input.

Apparently we have to approximate the function and use it for the simulation.

Looking at visual representation I had two hypothesis:
1. First (and apparently chosen at the end) impression is that it looks like Gaussian Kernel
2. The first option above is too cuspidal (arrow-headed peak). Next best option was inverted parabola.

The analytical investigation and mathematical experiments in Wolfram Alpha and then Wolfram Cloud resulted in such approximation formulas:
1. Gaussian curve
![The Gaussian curve picture in Images folder](Images/GaussianApproximation.png)
2. Inverted parabola curve
![The Gaussian curve picture in Images folder](Images/ParabolaApproximation.png)

#### Mathematical notes
The notes are available as [Wolfram Cloud notebook](https://www.wolframcloud.com/obj/13406c33-e24d-433b-89bf-a25c91523a9d).

The notebook [source code](https://www.wolframcloud.com/env/for.key/normpdf.nb).

To ease access it was exported to pdf [online](https://www.wolframcloud.com/pdf/d369b39dc4094799a1e20dc84120b9a1) and [locally](FunctionApproximationByWolframCloud.pdf)

#### Python representation
1. Gaussian curve
```python
    x = np.arange(0, 24, step, float)
    y = max_value * 1/(sigma * np.sqrt(2 * np.pi)*0.1336) \
        * np.exp(- (x - mu)**2 / (2 * sigma**2))
```
2. Inverted parabola curve
```python
    x = np.arange(0, 24, step, float)
    y = max_value - 70 * (mu - x * 1.0574) ** 2
```

After several experiments I gave preference to Gaussian combined with two simple lines (left and right endings) to cut the Gaussian long tails.


