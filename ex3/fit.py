import numpy as np 
import matplotlib.pyplot as plt 
from scipy import interpolate
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d, CubicSpline,pchip_interpolate

def func1(x,C,B):
    return B - C*x  

def func2(x,C,B):
    return x/C - B/C 

def func(x,a,b):
    return a*x + b



data = np.genfromtxt("results.dat")

beta = 0.325
rhol = data[:,1]
rhov = data[:,2]
temps = data[:,0]

y = rhol - rhov 
y = y ** (1./beta)

popt,pcov = curve_fit(func1,temps, y)
A = popt[0]
B = popt[1]
Tc = B/A 

y = 0.5*(rhol + rhov)
popt,pcov = curve_fit(func,Tc - temps,y)
A = popt[0]
rhoc = popt[1]

print(A,rhoc)
print(temps)

func = interp1d(y,temps,fill_value="extrapolate")

newx = np.concatenate((np.flip(y),[rhoc]))
print(func(rhoc))

criticalT = [Tc]
criticalrho = [rhoc]

plt.figure()
rho = np.concatenate((data[:,2],[rhoc],np.flip(data[:,1])))
newT = np.concatenate((data[:,0],[Tc],np.flip(data[:,0])))

plt.plot(rho,newT,marker="o",ms="7.5",ls="none",color="red")
plt.plot(y,temps,marker="o")
plt.plot(newx,func(newx),ls="--",color="black")

#for making coexisting area 
newrho = np.linspace(rho.min(), rho.max(), 50)
y = cubic_interpolation_model = pchip_interpolate(rho, newT, newrho)

plt.plot(newrho,y,ls="--",color="red")

plt.text(0.1, 0.7, r'V + L', fontsize = 22)
plt.text(0., 1.2, r'V', fontsize = 22)
plt.text(0.8, 1.2, r'L', fontsize = 22)
plt.text(0.22, 1.25, r'$\rho_c$,$T_c$', fontsize = 18)

plt.ylim(0.3,1.5)
plt.xlim(-0.1,1)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.minorticks_on()
plt.xlabel(r"$\rho$",fontsize=22)
plt.ylabel(r"$T$",fontsize=22)
plt.tight_layout()


#plt.savefig("phase-diagram-forgimp.svg", format='svg', dpi=1200)


plt.show()