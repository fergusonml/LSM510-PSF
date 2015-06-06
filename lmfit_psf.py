#!/usr/bin/env python
#requires python27, numpy, lmfit, xlrd
from lmfit import minimize, Parameters, Parameter, report_fit
import numpy as np
import pandas as pd
import os

# define objective function: returns the array to be minimized
def fcn2min(params, x, data):
    """ model exp(-2*x^2/w0^2), subtract data"""
    amp = params['amp'].value
    w0= params['w0'].value
    shift = params['shift'].value
    offset= params['offset'].value

    model = amp * np.exp(-2.0*(x-shift)*(x-shift)/w0/w0)+offset
    return model - data
 
def lmfit_psf(filename, wsname):
 a=pd.read_excel(filename,wsname,header=None)
 x=np.array(map(float,a[0]))
 data=np.array(map(float,a[1]))
 
 # create a set of Parameters
 params = Parameters()
 params.add('amp',   value= 100, min=0.0)
 params.add('w0', value=0.25, min=0.0)
 params.add('shift', value=0.35)
 params.add('offset', value= 0.0, min=0.0)
 
 
 # do fit, here with leastsq model
 result = minimize(fcn2min, params, args=(x, data))
 
 # calculate final result
 final = data + result.residual
 
 # write error report
 report_fit(params)
 
 # try to plot results
 try:
     import pylab
     pylab.plot(x, data, 'k+')
     pylab.plot(x, final, 'r')
     pylab.title('%s w0=%snm'%(os.path.splitext(filename)[0],round(params['w0'].value*1000)))
     pylab.draw()
 except:
     pass
 
#<end of examples/doc_basic.py>
