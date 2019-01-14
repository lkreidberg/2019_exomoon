import numpy as np
import matplotlib.pyplot as plt
import pickle

err = 379.e-6
chi2min = 201.38

plt.figure(figsize = (8.5,4))

plt.subplot(221)
plt.title("Data from this work")
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open("lk_fits/lk_lsq_nomoon.p", "rb"))
plt.plot(phase, data_nosys, '.k')
plt.plot(t_hr, fit_hr, color = 'b', label = 'no moon')
chi2 = np.sum((norm_resid/err)**2) 
ax = plt.gca()
ax.text( 0.03, 0.27,
        '$\Delta_{\chi^2_\\nu} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        + 'rms = ' + '{0:0d}'.format(int(rms)), 
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10
)
plt.xlim(-0.0035, 0.0035)
plt.axvline(0.0016925, linestyle = 'dotted', color = '0.5')
plt.gca().set_xticklabels([])
plt.legend(loc = 'lower right')
plt.ylabel("Relative flux")

plt.subplot(223)
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open("lk_fits/lk_lsq_moon.p", "rb"))
plt.plot(phase, data_nosys, '.k')
plt.plot(t_hr, fit_hr, color = 'r', label = 'moon')
chi2 = np.sum((norm_resid/err)**2) 
ax = plt.gca()
ax.text( 0.03, 0.27,
        '$\Delta_{\chi^2_\\nu} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        + 'rms = ' + '{0:0d}'.format(int(rms)), 
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10
)
plt.xlim(-0.0035, 0.0035)
plt.axvline(0.0016925, linestyle = 'dotted', color = '0.5')
plt.ylabel("Relative flux")
plt.xlabel("Orbital phase")
plt.legend(loc = 'lower right')


plt.subplot(222)
plt.title("Data from T&K (2018)")
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open("teachey_fits/lsq_teachey_nomoon.p", "rb"))
plt.plot(phase, data_nosys, '.k')
plt.plot(t_hr, fit_hr, color = 'b', label = 'no moon')
chi2 = np.sum((norm_resid/err)**2) 
ax = plt.gca()
ax.text( 0.03, 0.27,
        '$\Delta_{\chi^2_\\nu} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        + 'rms = ' + '{0:0d}'.format(int(rms)), 
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10
)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.axvline(0.0016925, linestyle = 'dotted', color = '0.5')
plt.xlim(-0.0035, 0.0035)
plt.legend(loc = 'lower right')

plt.subplot(224)
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open("teachey_fits/lsq_teachey_moon.p", "rb"))
plt.plot(phase, data_nosys, '.k')
plt.plot(t_hr, fit_hr, color = 'r', label = 'moon')
plt.legend(loc = 'lower right', fontsize = 10)
chi2 = np.sum((norm_resid/err)**2)
ax = plt.gca()
ax.text( 0.03, 0.27,
        '$\Delta_{\chi^2_\\nu} = $' + '{0:0.1f}'.format(chi2red_rms395 - chi2min)   + '\n'
        + 'rms = ' + '{0:0d}'.format(int(rms)), 
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
