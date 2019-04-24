import numpy as np
import mycorner as corner
import matplotlib.pyplot as plt

def quantile(x, q): return np.percentile(x, [100. * qi for qi in q])


"""chain = np.load("mcmc_output/mcmc_LK_6par.npy")
ndim = chain.shape[-1]
samples_lk = chain[:, 2000:10000, :].reshape((-1, ndim))"""
#samples_lk = samples_lk[:,[6,8]]

chain = np.load("mcmc_output/mcmc_LK_correct_for_referee.npy")
chain[0,:] -= 2458055.
ind = chain[2,:] == 1
chain = chain[:,ind]
samples_lk = chain[[0,1], :]
samples_lk = samples_lk.T

"""chain = np.load("mcmc_output/mcmc_TK18_6par.npy")
ndim = chain.shape[-1]
samples_tk = chain[:, 2000:10000, :].reshape((-1, ndim))
samples_tk = samples_tk[:,[6,8]].T"""

chain = np.load("mcmc_output/mcmc_TK18_correct_for_referee.npy")
ind = chain[2,:] == 1
chain = chain[:,ind]
chain[0,:] -= 2458055.
samples_tk = chain[[0,1], :]


print("LK shape", samples_lk.shape)
print("TK shape", samples_tk.shape)
#print("samples TK meds", np.median(samples_tk[0,:]), np.median(samples_tk[1,:]))
#samples_lk[:,1] = samples[

corner.corner(samples_lk, samples_tk, plot_datapoints = False, 
            levels = [0.68, 0.95, 0.997], fill_contours = True, alpha = 1.0, 
            color = 'blue', 
            range = [(-0.25,1.5), (0,5)],
            labels = ["Moon mid-transit time\n(BJD$_\mathrm{TDB}$ - 2458055)", 
            "Moon radius (R$_\oplus$)"]) 

print("LK rp 2, 3 sig", quantile(samples_lk[:, 1], [0.95, 0.997]))
print("TK, 16, 50, 84th perc", quantile(samples_tk[1, :], [0.16, 0.5, 0.84]))
print("t0_lk", quantile(samples_lk[:, 0], [0.16, 0.5, 0.84]) + 2458055.)
print("t0_tk", quantile(samples_tk[0, :], [0.16, 0.5, 0.84]) + 2458055.)
print(samples_lk[:,0].shape)
plt.savefig('fig5_pairs.pdf')
