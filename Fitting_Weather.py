# Created by Hope Murphy
# Assignment #5, problem 1


from math import cos, pi
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as p


# Read in data file
d = np.loadtxt(open("munich_temperatures_average_with_bad_data.txt"))
t= d[:,0]
data= d[:,1]

# Guess paraeters for a, b, c
guess_a= 20.0 #amplitude
guess_b= 0.0 #phase shift
guess_c= 5.0 #offset
guess_o= 1.0 #frequency
# print(data)

p0= [guess_o, guess_a, guess_b, guess_c]

#Create the function we want to fit
def F_t(x, omega, a, b, c):
	return np.cos((omega*x)+b)*a +c

# Omitt outliers by creating boolean loop
cut = np.logical_and(data > -50, data < 50)
#data2 = d[cut]
t2 = t[cut]
data2 = data[cut]

#print(d.shape)
#print(data2.shape)

# Do the fit
fit= curve_fit(F_t, t2, data2, p0=p0)


#Use this to plot our first estimate. This might be good enough. 
data_first_guess= F_t(t, *p0)

#Recreate the fitting curve using the optimized parameters
data_fit= F_t(t, *fit[0])


years = np.linspace(1994.,2020., 1000)

p.plot(t2, data2, '.')
p.plot(years, F_t(years, *fit[0]), label='After fitting')
p.plot(years, F_t(years, *p0), label='First guess')
p.xlim([1994,2014])
p.ylim([-20,30])
p.legend()
p.show()
