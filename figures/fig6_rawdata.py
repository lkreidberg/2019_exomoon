import numpy as np
import matplotlib.pyplot as plt


d = np.genfromtxt("lc_kep1625_kreidberg.txt")
#d = np.genfromtxt("lc_kep1625_kreidberg_rot_1_16_19.txt")
ind = np.arange(len(d))                                                
d = d[(ind!=106)&(ind!=115)&(ind != 0)&(ind!=124)&(ind!=125)] 


plt.subplot(211)
med = np.median(d[0:50, 1])

plt.plot(d[:,0] - np.min(d[:,0]), d[:,1]/1.e6, '.b', alpha = 0.5, label = "This work")


e = np.genfromtxt("prehook_correction_discrete.dat")
med = np.median(e[0:50, 1])
plt.plot(e[:,0] - np.min(e[:,0]), e[:,1]*290.776306/1.e6, '.r', alpha = 0.5, label = "TK18")
plt.ylabel("Photoelectrons ($\\times10^6$)")

plt.legend(loc = 'lower right')
plt.ylim(9, 9.4)


plt.subplot(212)

plt.ylabel("Difference (e-$\\times10^6$)")
plt.xlabel("Time since first exposure (days)")
plt.plot(d[:,0] - np.min(d[:,0]), (d[:,1] - e[:,1]*290.776306)/1.e6, '.k', label = "difference")

plt.tight_layout()
plt.savefig("fig6_rawdata.pdf")
