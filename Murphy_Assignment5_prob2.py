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


# Omitt outliers by creating boolean loop
#cut2 = np.logical_and(stars > -400, stars < 400)
#stars2 = stars[cut2]
#t2 = t[cut2]
#data2 = data[cut2]


# Fit VHELIO_AVG(VERR) vs. GLON(no error needed)
#	Fit three differenet functions: 1) Linear 2) Quadratic fit 3) Periodic (sin or cos)
y = stars['VHELIO_AVG']
x = stars['GLON']


def linear(x, m, b):
	return m*x+b
 
popt, pcov = curve_fit(linear, x, y) 


def quadratic_line(x, c, d, e):
	return c*(x**2)+d*x+e
 
popt2, pcov2 = curve_fit(quadratic_line, x, y) 


xlin = np.linspace(0., 360., 360)



guess_a= 15.0 #amplitude
guess_b= 10.0 #phase shift
guess_c= 5.0 #offset
guess_o= 6.0 #frequency
# print(data)

p0= [guess_o, guess_a, guess_b, guess_c]

#Create the function we want to fit
def F_t(x, omega, a, b, c):
	return np.cos((omega*x)+b)*a +c


# Do the fit
fit= curve_fit(F_t, x, y, p0=p0)


#Use this to plot our first estimate. This might be good enough. 
data_first_guess= F_t(x, *p0)

#Recreate the fitting curve using the optimized parameters
data_fit= F_t(x, *fit[0])




# Generate plots
p.plot(x, y, '.')  
p.plot(xlin, linear(xlin, popt[0], popt[1]), label='Linear fit') # Linear
p.plot(xlin, quadratic_line(xlin, popt2[0], popt2[1], popt2[2]), label='Quadratic fit')  # Quadratic fit
p.plot(xlin, F_t(xlin, *p0), label='First guess')
p.plot(xlin, F_t(xlin, *fit[0]), label='After fitting')  # Periodic (sin or cos)
p.legend()
p.xlim([0,360])
p.ylim([-400,400])
p.xlabel('GLON(no error needed)')
p.ylabel('VHELIO_AVG(VERR)')
p.title('VHELIO_AVG(VERR) vs. GLON(no error needed)')
p.show()
