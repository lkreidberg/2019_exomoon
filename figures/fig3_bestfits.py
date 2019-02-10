import numpy as np
import matplotlib.pyplot as plt
import pickle
from scipy.stats import f, norm

def get_significance(chi2ratio, df1, df2):
	alpha = (1. - f.cdf(chi2ratio, df1, df2))/2.
	z = norm.ppf(1.-alpha)
	return z

err = 367.e-6
moon_ingress = 1.25
period = 287.378949 
xmin, xmax = -0.3, 1.7
npoints = 219   #number of data points

#teachey_dir = "teachey_fits/"
#teachey_dir = "teachey_fits_xydecorr/"
#teachey_dir = "teachey_fits_poly2d_tophat/"
teachey_dir = "teachey_fits_full/"
lk_dir = "lk_fits_full/"

plt.figure(figsize = (8.5,4))

plt.subplot(221)
plt.title("This Work")
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395, dof_nomoon, nfree= pickle.load(open(lk_dir + "no_moon.p", "rb"), encoding='latin1')
plt.plot(period*phase - period*np.min(phase), data_nosys, '.w', markeredgecolor = 'k')
plt.plot(period*(t_hr) - period*np.min(phase), fit_hr, color = 'b', label = 'no moon', linewidth = 2.)
chi2 = np.sum((norm_resid/err)**2) 

npoints = len(phase)
nfreepar = npoints - dof_nomoon
BIC_LK_nomoon = chi2 + nfreepar*np.log(npoints)
BIC = chi2 + nfreepar*np.log(npoints)
ax = plt.gca()
ax.text( 0.03, 0.52,
        '$\mathrm{rms} =$' + '{0:0.1f}'.format(rms) + '\n' 
        + '${\chi^2} = $' + '{0:0.1f}'.format(chi2) + '\n'
        + '$\mathrm{dof} =$' + '{0:0d}'.format(int(dof_nomoon)) + '\n'
        #+ '$\Delta\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC - BIC_LK_nomoon),
        + '$\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC),    
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10,
        bbox=dict(facecolor='none', edgecolor='0.8')
)
plt.xlim(xmin, xmax)
plt.axvline(moon_ingress, linestyle = 'dotted', color = '0.5')
plt.gca().set_xticklabels([])
plt.legend(loc = 'lower right')
plt.ylabel("Relative flux")
chi2nu_lk_nomoon = chi2/dof_nomoon

plt.subplot(223)
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395, dof_moon, nfree = pickle.load(open(lk_dir + "moon.p", "rb"), encoding='latin1')
plt.plot(period*(phase - np.min(phase)), data_nosys, '.w', markeredgecolor = 'k')
plt.plot(period*(t_hr - np.min(phase)), fit_hr, color = 'b', label = 'moon', linewidth = 2.)
chi2 = np.sum((norm_resid/err)**2) 
#dof_moon -= 8   #accounting for fixed c1 - c9, but free c
nfreepar = npoints - dof_moon
BIC = chi2 + nfreepar*np.log(npoints)
ax = plt.gca()
ax.text( 0.03, 0.52,
        '$\mathrm{rms} =$' + '{0:0.1f}'.format(rms) + '\n' 
        + '${\chi^2} = $' + '{0:0.1f}'.format(chi2) + '\n'
        + '$\mathrm{dof} =$' + '{0:0d}'.format(int(dof_moon)) + '\n'
        #+ '$\Delta\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC - BIC_LK_nomoon),
        + '$\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC),    
        verticalalignment='top',horizontalalignment='left',
        transform=ax.transAxes, fontsize = 10,
        bbox=dict(facecolor='none', edgecolor='0.8')
)
plt.xlim(xmin, xmax)
plt.axvline(moon_ingress, linestyle = 'dotted', color = '0.5')
plt.ylabel("Relative flux")
plt.xlabel("Time since first exposure (BJD$_\mathrm{TDB}$)")
plt.legend(loc = 'lower right')
chi2nu_lk_moon = chi2/dof_moon

print(chi2nu_lk_nomoon, chi2nu_lk_moon, dof_nomoon, dof_moon)

chi2ratio = chi2nu_lk_moon/chi2nu_lk_nomoon

print("significance", get_significance(chi2ratio, dof_moon, dof_nomoon))

plt.subplot(222)
plt.title("Teachey & Kipping (2018)")
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open(teachey_dir + "lsq_teachey_nomoon.p", "rb"))
plt.plot(period*(phase - np.min(phase)), data_nosys, '.w', markeredgecolor = 'k')
plt.plot(period*(t_hr - np.min(phase)), fit_hr, color = 'r', label = 'no moon', linewidth = 2.)
chi2 = np.sum((norm_resid/err)**2) 
dof_nomoon = 202
nfreepar = npoints - dof_nomoon
BIC = chi2 + nfreepar*np.log(npoints)
ax = plt.gca()
ax.text( 0.03, 0.52,                                                            
        '$\mathrm{rms} =$' + '{0:0.1f}'.format(rms) + '\n'                      
        + '${\chi^2} = $' + '{0:0.1f}'.format(chi2) + '\n'                      
        + '$\mathrm{dof} =$' + '{0:0d}'.format(int(dof_nomoon)) + '\n'            
        #+ '$\Delta\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC - BIC_LK_nomoon),    
        + '$\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC),    
        verticalalignment='top',horizontalalignment='left',                     
        transform=ax.transAxes, fontsize = 10,
        bbox=dict(facecolor='none', edgecolor='0.8')
)  
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.axvline(moon_ingress, linestyle = 'dotted', color = '0.5')
plt.xlim(xmin, xmax)
plt.legend(loc = 'lower right')

plt.subplot(224)
phase, data_nosys, norm_resid, t_hr, fit_hr, rms, rms_predicted, chi2, chi2red, chi2red_rms395 = pickle.load(open(teachey_dir + "lsq_teachey_moon.p", "rb"))
plt.plot(period*(phase - np.min(phase)), data_nosys, '.w',  markeredgecolor = 'k') 
plt.plot(period*(t_hr - np.min(phase)), fit_hr, color = 'r', label = 'moon', linewidth = 2.) 
plt.legend(loc = 'lower right', fontsize = 10)
chi2 = np.sum((norm_resid/err)**2)
dof_moon = 196                                                                
nfreepar = npoints - dof_moon                                                     
BIC = chi2 + nfreepar*np.log(npoints)  
ax = plt.gca()
ax.text( 0.03, 0.52,                                                            
        '$\mathrm{rms} =$' + '{0:0.1f}'.format(rms) + '\n'                      
        + '${\chi^2} = $' + '{0:0.1f}'.format(chi2) + '\n'                      
        + '$\mathrm{dof} =$' + '{0:0d}'.format(int(dof_moon)) + '\n'            
        #+ '$\Delta\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC - BIC_LK_nomoon),    
        + '$\mathrm{BIC} =$' + '{0:0.1f}'.format(BIC),    
        verticalalignment='top',horizontalalignment='left',                     
        transform=ax.transAxes, fontsize = 10,
        bbox=dict(facecolor='none', edgecolor='0.8')
)  
plt.gca().set_yticklabels([])
plt.axvline(moon_ingress, linestyle = 'dotted', color = '0.5')
plt.xlim(xmin, xmax)
plt.xlabel("Time since first exposure (BJD$_\mathrm{TDB}$)")


plt.tight_layout()

plt.savefig("fig3_bestfits.pdf")
#plt.show()
