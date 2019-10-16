import matplotlib.pyplot as plt
import numpy as np
import math as m
import matplotlib.colors as mcolors
import matplotlib.image as mpimg 
from tkinter import *
import matplotlib as mp



map_img = mpimg.imread('floorplan.png')

c = 299792458 #m/s

size = 750 # number of points
space = []
center = [size/2,size/2]
for i in range (0,size):
    space.append([])
for j in range (0,size):
    for k in range (0,size):
        space[j].insert(k,0)

# plotting a point
def point(pos,val):
    x = pos[0]
    y = pos[1]
    space[y][x] += val

    
def freespace_1ptdb(pos,    #position of antenna
                    f,      #frequency
                    ppos):  #point position
    l = c/f
    x = abs(pos[0]-ppos[0])
    y = abs(pos[1]-ppos[1])
    r = m.sqrt(m.pow(x,2)+m.pow(y,2))
    if x==0 and y==0:
        val = -20*m.log10(4*m.pi*.1/l)
    else:
        val = -20*m.log10(4*m.pi*r/l)
    point(ppos,val)

def freespace_rad(x,y,f):
    pos = [x,y]
    center = [size/2,size/2]
    for i in range(0,size):
        for j in range(0,size):
            freespace_1ptdb(pos,f*1000,[i,j])




#
# mp.axes.Axes.contains(mouseevent)
#freespace_rad(200,200,1000000000000)

colors = [(1,0,0,c) for c in np.linspace(0,1,100)]
cmapred = mcolors.LinearSegmentedColormap.from_list('mycmap', colors, N=5)

plt.imshow(map_img,
          #aspect = plt.get_aspect(),
          #extent = plt.get_xlim() + plt.get_ylim(),
          zorder = 1) #put the map under the heatmap


#plt.subplot(111)

#mouseevent = freespace_rad(event.xdata,event.ydata

def onclick(event):
    print(event.xdata, event.ydata)
    freespace_rad(event.xdata, event.ydata,3700)




plt.imshow(space, cmap=cmapred,interpolation='bilinear',zorder = 2)
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)

plt.show()

