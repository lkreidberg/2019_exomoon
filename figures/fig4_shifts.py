import numpy as np                                                              
import matplotlib.pyplot as plt 


a1= 9.9706e-01 	 
a2= 9.9901e-01 	
a3= 9.9923e-01 
a4= 9.9951e-01
a5= 9.9952e-01 
a6= 9.9976e-01 
a7= 9.9978e-01 
a8= 9.9984e-01
a9= 1.0000e+0

a_s = [0., a1, a2, a3, a4, a5, a6, a7, a8, a9]

c = 10.**6.9693

a = 1.4788e-03 	 
b = -1.0032e-02  

d = np.genfromtxt("raw_orbnum.txt")

t = d[:,0]
f = d[:,1]/c
expnum = d[:,2]
xshifts = d[:,3]/45.
yshifts = d[:,4]
orbnum = d[:,5]

for i in np.arange(9): 
    ind = expnum == i
    f[ind] /= a_s[int(i)]

sys = 1. + a*xshifts + b*yshifts

f /= sys

plt.figure(figsize = (4,5))

plt.subplot(211)
plt.plot(t - np.min(t), xshifts, '.k', alpha = 0.5, label = "spectral")
binf = []
bint = []
for i in range(24):
    ind = orbnum == i
    binf.append(np.mean(xshifts[ind]))
    bint.append(np.mean(t[ind] - np.min(t)))
#plt.plot(np.array(bint), np.array(binf), 'or')

plt.ylabel("Spectral shift (pixels)")

plt.subplot(212)
plt.plot(t - np.min(t), yshifts, '.k', alpha = 0.5, label = "spatial")

binf = []
bint = []
for i in range(24):
    ind = orbnum == i
    binf.append(np.mean(yshifts[ind]))
    bint.append(np.mean(t[ind] - np.min(t)))
#plt.plot(np.array(bint), np.array(binf), 'or')

plt.ylabel("Spatial shift (pixels)")

plt.xlabel("Time from first exposure (days)")


plt.tight_layout()
plt.savefig('fig4_shifts.pdf')
#plt.show()
