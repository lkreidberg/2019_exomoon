import numpy as np
import matplotlib.pyplot as plt

d = np.genfromtxt("12_26_23_33/diagnostics.txt")

plt.subplot(311)
plt.plot(d[:,1] - np.min(d[:,1]), d[:,3], '.k')
plt.ylabel("Background (e-)")

plt.subplot(312)
plt.plot(d[:,1]- np.min(d[:,1]), (d[:,4] - np.median(d[:,4]))/45., '.k')
plt.ylim(-0.2,0.2)
plt.ylabel("Spectral shift (pix)")

plt.subplot(313)
plt.plot(d[:,1]- np.min(d[:,1]), 1.*(d[:,5] - np.mean(d[:,5])), '.k')
plt.ylim(-0.2,0.2)
plt.ylabel("Spatial shift (pix)")

plt.xlabel("Time (days since first exposure)")

plt.tight_layout()
plt.show()
