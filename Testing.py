# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:08:18 2024

@author: ahmed
"""

import numpy as np
import matplotlib.pyplot as pt

def sinefunction(z, graph): 
    graph.set_title("Sine Function Graph")
    x = 0 
    while (x < z):
        graph.scatter(x, np.sin(x))
        x = x + 0.1
    graph.set_xlabel("angle value")
    graph.set_ylabel("function value") 
 
    
def cosinefunction(z, graph): 
    
    graph.set_title("Cosine Function Graph")
    x = 0 
    xValues = []
    yValues = []
    while (x < z):
        xValues.append(x)
        yValues.append(np.cos(x))
        x = x + 0.1
    graph.plot(xValues,yValues)
    graph.set_xlabel("angle value")
    graph.set_ylabel("function value") 
    
            
    
    

fig, b = pt.subplots(1)
fig, a = pt.subplots(1)
#fig c = pt.subplots(2)
pt.subplots_adjust(left  = 0.125, right = 0.9, bottom = 0.1, top = 0.9, wspace = 0.2, hspace = 0.45)

sinefunction((np.pi)*2, b) #c[0]
cosinefunction((np.pi)*2, a) #c[1]

pt.show()