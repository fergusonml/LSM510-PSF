#!/usr/bin/env python
from lmfit_psf import *
import matplotlib.pyplot as plt
import pylab

#os.system("ipython lmfit_psf0.py")
#os.system("ipython lmfit_psf2.py")

filename=[\
#'200nmbead100x_1a.xlsx',\
#'200nmbead100x_1b.xlsx',\
#'200nmbead100x_1c.xlsx',\
'200nmbead40x_1a.xlsx',\
'200nmbead100x_2a.xlsx',\
'200nmbead100x_2b.xlsx',\
'200nmbead100x_2c.xlsx',\
'200nmbead100x_3.xlsx',\
#'200nmbead100x_4.xlsx'\
]
sheet=[\
'Sheet1',\
'Sheet2',\
'Sheet3'\
]

nrows=len(filename)
ncols=len(sheet)

fig,axes=plt.subplots(nrows=nrows,ncols=ncols,figsize=(12,8))
plt.suptitle('PSF measurements')

for i in range(nrows):
 for j in range(ncols):
    plt.subplot(nrows,ncols,(i)*ncols+(j+1))
    lmfit_psf(filename[i],sheet[j])    

pylab.show()
