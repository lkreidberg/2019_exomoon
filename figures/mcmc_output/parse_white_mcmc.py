import sys                                                                      
import pickle                                                                   
import os                                                                       
import glob                                                                     
import numpy as np                                                              
import matplotlib.pyplot as plt 
import corner

def quantile(x, q): return np.percentile(x, [100. * qi for qi in q]) 


ndim = 15
chain = np.load("mcmc_TK18_6par.npy")

samples = chain[:, 2000:10000, :].reshape((-1, ndim))


medians, err_hi, twosig, threesig, err_lo = [], [], [], [], []

for i in range(ndim):
        q = quantile(samples[:, i], [0.16, 0.5, 0.84, 0.95, 0.997])
        medians.append(q[1])
        err_hi.append(q[2] - q[1])
        err_lo.append(q[1] - q[0])
        twosig.append(q[3])
        threesig.append(q[4])
        print(medians[i], err_lo[i], err_hi[i])

print("moon 2sig, 3sig:", twosig[8], threesig[8])
print("moon med/err:", medians[8], err_lo[8], err_hi[8])




