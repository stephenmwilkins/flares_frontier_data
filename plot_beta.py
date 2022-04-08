

import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt

data = ascii.read('beta.dat')

print(data)



# --- redshift evolution

fig, ax = plt.subplots()

for z in np.arange(10.,15.,1.):
    ax.plot(data['log10LFUV'], data[f'beta_z{z}_P50.0'], label=f'z={z}')

ax.legend()
ax.set_xlabel(r'$\log_{10}(L_{FUV}/erg\ s^{-1}\ Hz^{-1})$')
ax.set_ylabel(r'$\beta$')

plt.show()
fig.clf()


# --- show percentile ranges

fig, ax = plt.subplots()

z = 10.

ax.fill_between(data['log10LFUV'], data[f'beta_z{z}_P2.2'], data[f'beta_z{z}_P97.8'], color='b', alpha = 0.2)
ax.fill_between(data['log10LFUV'], data[f'beta_z{z}_P15.8'], data[f'beta_z{z}_P84.2'], color='b', alpha = 0.2)
ax.plot(data['log10LFUV'], data[f'beta_z{z}_P50.0'],c='b', label='$P_{50}$')

ax.set_xlabel(r'$\log_{10}(L_{FUV}/erg\ s^{-1}\ Hz^{-1})$')
ax.set_ylabel(r'$\beta$')

plt.show()
