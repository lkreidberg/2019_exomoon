import numpy as np
import matplotlib.pyplot as plt
import pickle
import glob, os
from matplotlib import rc


# COMPUTE ROOT-MEAN-SQUARE AND STANDARD ERROR OF DATA FOR VARIOUS BIN SIZES
def computeRMS(data, maxnbins=None, binstep=1, isrmserr=False):
    #data    = fit.normresiduals
    #maxnbin = maximum # of bins
    #binstep = Bin step size

    # bin data into multiple bin sizes
    npts    = data.size
    if maxnbins is None:
        maxnbins = npts/11.
    binsz   = np.arange(1, maxnbins+binstep, step=binstep)
    nbins   = np.zeros(binsz.size)
    rms     = np.zeros(binsz.size)
    rmserr  = np.zeros(binsz.size)
    for i in range(binsz.size):
        nbins[i] = int(np.floor(data.size/binsz[i]))
        bindata   = np.zeros(int(nbins[i]), dtype=float)
        # bin data
        # ADDED INTEGER CONVERSION, mh 01/21/12
        for j in range(int(nbins[i])):
            bindata[j] = data[int(j*binsz[i]):int((j+1)*binsz[i])].mean()
        # get rms
        rms[i]    = np.sqrt(np.mean(bindata**2))
        rmserr[i] = rms[i]/np.sqrt(2.*int(nbins[i]))
    # expected for white noise (WINN 2008, PONT 2006)
    stderr = (data.std()/np.sqrt(binsz))*np.sqrt(nbins/(nbins - 1.))
    if isrmserr == True:
        return rms, stderr, binsz, rmserr
    else:
        return rms, stderr, binsz


# Compute standard error
def computeStdErr(datastd, datasize, binsz):
    #datastd  = fit.normresiduals.std()
    #datasize = fit.normresiduals.size
    #binsz    = array of bins

    nbins   = np.zeros(binsz.size)
    for i in range(binsz.size):
        nbins[i] = int(np.floor(datasize/binsz[i]))
    stderr = (datastd/np.sqrt(binsz))*np.sqrt(nbins/(nbins - 1.))
    return stderr



plt.figure(figsize = (4,3.5))

chi2red = 1.05   #best fit chi2 (need to scale for photon noise)

d = np.genfromtxt("kreidberg_nomoon_resid.txt")
ind = np.argsort(d[:,0])
d = d[ind]
resid = d[:,1]
rms, stderr, binsz, rmserr = computeRMS(resid, maxnbins = None, binstep = 1, isrmserr = True)
normfactor = stderr[0]
#normfactor = m.rms_predicted
plt.loglog(binsz, stderr/normfactor, color='black', ls='-', label='Expected  rms', zorder = -1) # expected noise
#print(stderr/normfactor)
plt.loglog(binsz, rms/normfactor*np.sqrt(chi2red), zorder = 10, color='blue', label='This work, no-moon')    # our noise

print("excess over photon, LK:", binsz) 
print("excess over photon, LK:", rms*np.sqrt(chi2red)/stderr)
stderr_LK = np.copy(stderr)

d = np.genfromtxt("kreidberg_moon_resid.txt")                                 
ind = np.argsort(d[:,0])                                                        
d = d[ind]                                                                      
resid = d[:,1]                                                                  
rms, stderr, binsz, rmserr = computeRMS(resid, maxnbins = None, binstep = 1, isrmserr = True)
normfactor = stderr[0]                                                          
plt.loglog(binsz, rms/normfactor*np.sqrt(chi2red), color='blue', linestyle = 'dashed', label='This work, moon')    # our noise


d = np.genfromtxt("teachey_nomoon_resid.txt")
ind = np.argsort(d[:,0])
d = d[ind]
resid = d[:,1]
rms, stderr, binsz, rmserr = computeRMS(resid, maxnbins = None, binstep = 1, isrmserr = True)
#normfactor = m.rms_predicted
plt.loglog(binsz, rms/normfactor*np.sqrt(chi2red), color='red',  label='TK18, no-moon')    # our noise


print("excess over photon, teachey nom:", rms*np.sqrt(chi2red)/stderr_LK)



d = np.genfromtxt("teachey_moon_resid.txt")
ind = np.argsort(d[:,0])
d = d[ind]
resid = d[:,1]
rms, stderr, binsz, rmserr = computeRMS(resid, maxnbins = None, binstep = 1, isrmserr = True)
#normfactor = m.rms_predicted
plt.loglog(binsz, rms/normfactor*np.sqrt(chi2red), color='red',  linestyle = 'dashed', label='TK18, moon')    # our noise

print("excess over photon, teachey moon:", rms*np.sqrt(chi2red)/stderr_LK)

#plt.xlim(0, binsz[-1]*2)
plt.xlim(1, 20) 
plt.ylim(stderr[-1]/normfactor/2., 1.3) 

plt.xlabel("Data points per bin")
plt.ylabel("Normalized RMS") 
plt.legend(loc = 'lower left', fontsize = 10)

plt.gca().set_xticks([1, 10])
plt.gca().set_xticklabels([1, 10])
plt.gca().set_yticks([1, 0.1])
plt.gca().set_yticklabels([1, 0.1])

plt.gca().tick_params(axis='both', which='major', pad=2)

plt.tight_layout()
#plt.show()
plt.savefig("fig2_rms.pdf")
