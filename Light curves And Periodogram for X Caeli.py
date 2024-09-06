# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:04:19 2024

@author: ahmed
"""

import numpy as np
import matplotlib.pyplot as pt 
import lightkurve as lk 



def getLightCurveData(nameOfStar):
    x = lk.search_targetpixelfile(nameOfStar).download()
    y = x.to_lightcurve()
    y.remove_outliers()
    y.plot()
    #y.scatter()
    
    
def getPeriodogramData(nameOfStar): 
    x = lk.search_targetpixelfile(nameOfStar).download()
    y = x.to_lightcurve().remove_outliers()
    z = y.to_periodogram()
    z.plot()
    
    
#fig, a = pt.subplots(1)
getLightCurveData("X Caeli")
getPeriodogramData("X Caeli")
pt.show()


