# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:20:11 2024

@author: ahmed
"""

import spiceypy as sy
import numpy as np
import matplotlib.pyplot as pt 
import lightkurve as lk 

sy.furnsh('naif0012.tls')
sy.furnsh('orx_240210_290101_240410_od389-R-DSM3-P-DSM5_v1.bsp')
sy.furnsh('de440s.bsp')

def getTrajectory(starting, ending, ObjectName, OrbitingBody, Title): 
    step = 4000
    dates = [starting, ending]
    start = sy.str2et(dates[0])
    end = sy.str2et(dates[1])
    times = [x*(end-start)/step + start for x in range(step)]
    positions, lightTimes = sy.spkpos(ObjectName, times, 'J2000', 'NONE', OrbitingBody)
    sy.kclear
    positions = positions.T
    fig = pt.figure(figsize=(9, 9))
    ax  = fig.add_subplot(111, projection='3d')
    ax.plot(positions[0], positions[1], positions[2])
    pt.title(Title)
    pt.show()


getTrajectory("Feb 10 2024", "Dec 31, 2028", "OSIRIS-REX", "Earth",  "OSIRIS-REX Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Earth", "Sun",  "Earth Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Mercury", "Sun",  "Mercury Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Venus", "Sun",  "Venus Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Mars BARYCENTER", "Sun",  "Mars Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Jupiter BARYCENTER", "Sun",  "Jupiter Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Saturn BARYCENTER", "Sun",  "Saturn Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Uranus BARYCENTER", "Sun",  "Uranus Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Neptune BARYCENTER", "Sun",  "Neptune Trajectory Feb 10 2024 to Dec 30 2028")
getTrajectory("Feb 10 2024", "Dec 31, 2028", "Pluto BARYCENTER", "Sun",  "Pluto Trajectory Feb 10 2024 to Dec 30 2028")

