#!/usr/bin/env python
#<examples/doc_basic.py>
from lmfit import minimize, Parameters, Parameter, report_fit
import numpy as np
import pdb

# create data to be fitted
#x = np.linspace(0, 15, 301)
#data = (5. * np.sin(2 * x - 0.1) * np.exp(-x*x*0.025) +
#        np.random.normal(size=len(x), scale=0.2) )
from read_xlsx import *
a=read_xlsx('200nmbeadlsmpsfvalues.xlsx')
#x=np.array(map(float,a[0]))
#data=np.array(map(float,a[1]))
x=a[0]
data=a[1]

#print type(x),type(data)
#pdb.set_trace()

# define objective function: returns the array to be minimized
def fcn2min(params, x, data):
    """ model exp(-2*x^2/w0^2), subtract data"""
    amp = params['amp'].value
    w0= params['w0'].value
    shift = params['shift'].value
    offset= params['offset'].value

    model = amp * np.exp(-2.0*(x-shift)*(x-shift)/w0/w0)+offset
    return model - data

# create a set of Parameters
params = Parameters()
params.add('amp',   value= 35, min=0.0)
params.add('w0', value=0.25, min=0.0)
params.add('shift', value=0.5)
params.add('offset', value= 20.0, min=0.0)


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
    pylab.show()
except:
    pass

#<end of examples/doc_basic.py>
