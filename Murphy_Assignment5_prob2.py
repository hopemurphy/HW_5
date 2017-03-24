# Created by Hope Murphy
# Read me file includes written answers to questions


import matplotlib.pyplot as p
import fitsio
import numpy as np
from scipy.optimize import curve_fit

line_fit = []

Data = fitsio.FITS('allStar-l30e.2.fits')  #reference

# Fit the any trend in radial velocity versus position


# Select APOGEE stars only with 10 < GLAT < 12
# GLAT is data name
cut = Data[1].where('GLAT > 10 && GLAT <12')
stars=Data[1][cut]
#len(stars)


# Fit VHELIO_AVG(VERR) vs. GLON(no error needed)
#	Fit three differenet functions: 1) Linear 2) Quadratic fit 3) Periodic (sin or cos)
y = stars['VHELIO_AVG']
x = stars['GLON']

def linear(x, m, b):
	return m*x+b
 
popt, pcov = curve_fit(linear, x, y) 

xlin = np.linspace(0., 360., 360)

# Generate plots
p.plot(x, y, '.')  
p.plot(xlin, linear(xlin, popt[0], popt[1]), label='Linear fit') # Linear
p.xlim([0,360])
p.plot()  # Quadratic fit
p.plot()  # Periodic (sin or cos)

p.show()