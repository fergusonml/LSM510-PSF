# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print 'click', event
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

file='/Users/mattferguson/Google_Drive/Research/github/ISS beads/200nmbeads_Z_2001.bin'
simfcs=np.memmap(file, dtype=np.uint16,shape=(256,256))
fig = plt.figure()
plt.imshow(simfcs)
#plt.show()

#def onclick(event):
#    print 'button=%d, x=%d, y=%d'%(
#        event.button, event.x, event.y)

#cid = fig.canvas.mpl_connect('button_press_event', onclick)
ax = fig.add_subplot(111)
line, = ax.plot([0], [0])  # empty line
linebuilder = LineBuilder(line)

plt.show()

