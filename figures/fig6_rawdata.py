import numpy as np
import matplotlib.pyplot as plt

moon_ingress = 1.25

d = np.genfromtxt("lc_kep1625_kreidberg.txt")
#d = np.genfromtxt("lc_kep1625_kreidberg_rot_1_16_19.txt")
ind = np.arange(len(d))                                                
d= d[np.argsort(d[:,0])]
d = d[(ind!=106)&(ind!=115)&(ind != 0)&(ind!=124)&(ind!=125)] 
print("len lk", len(d[:,0]))


plt.figure(figsize = (4.5,4.5))
plt.subplot(211)
med = np.median(d[0:50, 1])

plt.plot(d[:,0] - np.min(d[:,0]), d[:,1]/1.e6, '.b', alpha = 0.5, label = "This work")
#plt.plot(d[:,0] - np.min(d[:,0]), np.log(d[:,1]), '.b', alpha = 0.5, label = "This work")


e = np.genfromtxt("prehook_correction_discrete.dat")
print("len tk", len(e[:,0]))
med = np.median(e[0:50, 1])
plt.plot(e[:,0] - np.min(e[:,0]), e[:,1]*290.776306/1.e6, '.r', alpha = 0.5, label = "TK18")
#plt.plot(e[:,0] - np.min(e[:,0]), np.log(e[:,1]*290.776306), '.r', alpha = 0.5, label = "TK18")
plt.ylabel("Photoelectrons ($\\times10^6$)")

plt.legend(loc = 'center right')
#plt.ylim(9, 9.4)


plt.subplot(212)

plt.ylabel("Difference (e-$\\times10^6$)")
plt.xlabel("Time since first exposure (days)")
plt.plot(d[:,0] - np.min(d[:,0]), (d[:,1] - e[:,1]*290.776306)/1.e6, '.k', label = "difference")
plt.axvline(moon_ingress, linestyle = 'dotted', color = '0.5')

plt.tight_layout()
plt.savefig("fig6_rawdata.pdf")
