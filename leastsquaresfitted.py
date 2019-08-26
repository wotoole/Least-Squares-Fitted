'''
Liam O'Toole
leastsquaresfitted.py
16 September 2014
'''
from numpy import *
from math import *
import matplotlib.pyplot as plt
#Record data values
N = input("enter the number of data points.")

#initialize sums
sum_x = 0
sum_y = 0
sum_xx = 0
sum_xy = 0
xmin = 0

#initialize lists
x = []
y = []


#get the number of data points from the user
N = input("Enter the number of data point.")

#initialize sums
sum_x = 0
sum_y = 0
sum_xx = 0
sum_xy = 0
xmin = 0

#initialize lists
x = []
y = []

#get the data values from user
for i in range (1, N + 1, 1):
    print "for point %s" %i
    x.append(input("Enter x:"))
    y.append(input("Enter y:"))

#perform our calculations
for i in range (1, N+1):
    if x[i-1] < xmin:
        xmin = x[i-1]
    sum_x = sum_x + x[i-1]
    sum_y = sum_y + y[i-1]
    xx = x[i-1]*x[i-1]
    sum_xx = sum_xx + xx
    xy = x[i-1]*y[i-1]
    sum_xy = sum_xy +xy

#calculate the coefficients
D = N*sum_xx - sum_x*sum_x
A = (sum_xx*sum_y - sum_x*sum_xy)/D
B = (N*sum_xy - sum_x*sum_y)/D

#Calculate uncertainties in y, A, and B
for i in range (1, N+1, 1):
    dev = y[i-1] - A - B*x[i-1]
    dev = dev*dev
sigy = sqrt(dev/(N-2))
sigA = sigy*sqrt(sum_xx/D)
sigB = sigy*sqrt(N/D)


#plot data points
#plt.scatter(x, y, c = "b", marker = "o")
plt.errorbar(x, y, yerr = sigy, fmt = 'bo')

#plot least squares fit line
xc = linspace(xmin, x[N-1], 10)
yc = A + B*xc
plt.plot(xc, yc, "r-")

print "The fitted straight line is y = (%s) + %sx"%(A, B)
print "The uncertainty in y is sigy = (%s)"%sigy
print "The uncertainty in A is sigA = (%s)"%sigA
print "The uncertainty in B is sigB = (%s)"%sigB
plt.show()
