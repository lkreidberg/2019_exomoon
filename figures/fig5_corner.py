import numpy as np
import mycorner as corner
import matplotlib.pyplot as plt

def quantile(x, q): return np.percentile(x, [100. * qi for qi in q])

chain = np.load("mcmc_output/mcmc_LK.npy")
ndim = chain.shape[-1]
samples_lk = chain[:, 1000:5000, :].reshape((-1, ndim))

chain = np.load("mcmc_output/mcmc_TK18.npy")
ndim = chain.shape[-1]
samples_tk = chain[:, 2000:10000, :].reshape((-1, ndim))

samples_lk = samples_lk[:,5:7]

samples_tk = samples_tk[:,5:7].T
corner.corner(samples_lk, samples_tk, plot_datapoints = False, 
            levels = [0.68, 0.95, 0.997], fill_contours = True, alpha = 0.5, 
            color = 'blue', 
            labels = ["Moon mid-transit time\n(BJD$_\mathrm{TDB}$ - 2458055)", 
            "Moon radius (R$_\oplus$)"]) 

print(quantile(samples_lk[:, 1], [0.95, 0.997]))
print(quantile(samples_tk[1, :], [0.003, 0.16, 0.5, 0.84]))
print(quantile(samples_tk[0, :], [0.16, 0.5, 0.84]) + 2458055.)
plt.savefig('fig5_pairs.pdf')
