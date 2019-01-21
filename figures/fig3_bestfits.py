import numpy as np
import matplotlib.pyplot as plt
import pickle
from scipy.stats import f, norm

def get_significance(chi2ratio, df1, df2):
	alpha = (1. - f.cdf(chi2ratio, df1, df2))/2.
	z = norm.ppf(1.-alpha)
	return z

err = 370.e-6
chi2min = 201.38

#teachey_dir = "teachey_fits/"
#teachey_dir = "teachey_fits_xydecorr/"
teachey_dir = "teachey_fits_poly2d_tophat/"
lk_dir = "lk_fits_new/"

plt.figure(figsize = (8.5,4))

plt.subplot(221)
plt.title("Data from this work")
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395, dof_nomoon = pickle.load(open(lk_dir + "no_moon.p", "rb"))
plt.plot(phase, data_nosys, '.w', markeredgecolor = 'k')
plt.plot(t_hr, fit_hr, color = 'b', label = 'no moon', linewidth = 2.)
chi2 = np.sum((norm_resid/err)**2) 
ax = plt.gca()
ax.text( 0.03, 0.27,
        #'$\Delta{\chi^2} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        '${\chi^2} = $' + '{0:0.1f}'.format(chi2)   + '\n'
        + 'rms = ' + '{0:0.1f}'.format(rms), 
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10
)
plt.xlim(-0.0035, 0.0035)
plt.axvline(0.0016925, linestyle = 'dotted', color = '0.5')
plt.gca().set_xticklabels([])
plt.legend(loc = 'lower right')
plt.ylabel("Relative flux")
chi2nu_lk_nomoon = chi2/dof_nomoon

plt.subplot(223)
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395, dof_moon = pickle.load(open(lk_dir + "moon.p", "rb"))
plt.plot(phase, data_nosys, '.w', markeredgecolor = 'k')
plt.plot(t_hr, fit_hr, color = 'b', label = 'moon', linewidth = 2.)
chi2 = np.sum((norm_resid/err)**2) 
ax = plt.gca()
ax.text( 0.03, 0.27,
#        '$\Delta{\chi^2} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        '${\chi^2} = $' + '{0:0.1f}'.format(chi2)   + '\n'
        + 'rms = ' + '{0:0.1f}'.format(rms), 
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10
)
plt.xlim(-0.0035, 0.0035)
plt.axvline(0.0016925, linestyle = 'dotted', color = '0.5')
plt.ylabel("Relative flux")
plt.xlabel("Orbital phase")
plt.legend(loc = 'lower right')
chi2nu_lk_moon = chi2/dof_moon

print(chi2nu_lk_nomoon, chi2nu_lk_moon, dof_nomoon, dof_moon)

chi2ratio = chi2nu_lk_moon/chi2nu_lk_nomoon

print("significance", get_significance(chi2ratio, dof_moon, dof_nomoon))

plt.subplot(222)
plt.title("Data from T&K (2018)")
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open(teachey_dir + "lsq_teachey_nomoon.p", "rb"))
plt.plot(phase, data_nosys, '.w', markeredgecolor = 'k')
plt.plot(t_hr, fit_hr, color = 'r', label = 'no moon', linewidth = 2.)
chi2 = np.sum((norm_resid/err)**2) 
ax = plt.gca()
ax.text( 0.03, 0.27,
        #'$\Delta{\chi^2} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        '${\chi^2} = $' + '{0:0.1f}'.format(chi2)   + '\n'
        + 'rms = ' + '{0:0.1f}'.format(rms), 
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10
)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.axvline(0.0016925, linestyle = 'dotted', color = '0.5')
plt.xlim(-0.0035, 0.0035)
plt.legend(loc = 'lower right')

plt.subplot(224)
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open(teachey_dir + "lsq_teachey_moon.p", "rb"))
plt.plot(phase, data_nosys, '.w',  markeredgecolor = 'k') 
plt.plot(t_hr, fit_hr, color = 'r', label = 'moon', linewidth = 2.) 
plt.legend(loc = 'lower right', fontsize = 10)
chi2 = np.sum((norm_resid/err)**2)
ax = plt.gca()
ax.text( 0.03, 0.27,
        #'$\Delta{\chi^2} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        '${\chi^2} = $' + '{0:0.1f}'.format(chi2)   + '\n'
        + 'rms = ' + '{0:0.1f}'.format(rms), 
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10
)
plt.gca().set_yticklabels([])
plt.axvline(0.0016925, linestyle = 'dotted', color = '0.5')
plt.xlim(-0.0035, 0.0035)
plt.xlabel("Orbital phase")


plt.tight_layout()

plt.savefig("fig3_bestfits.pdf")
#plt.show()
