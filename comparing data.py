# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:03:36 2020

@author: Osama
"""

import matplotlib.pyplot as plt
import numpy as np

STARTING_TOTAL_BLOBS = 200
STARTING_INFECTED_BLOBS = 3
HEALTHCARE_CAPACITY = 40
movement_range_1 = (-6, 7)
movement_range_2 = (-3, 4) 

time_1 = np.load(f"time_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{movement_range_1}.npy")
time_2 = np.load(f"time_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{movement_range_2}.npy")
infected_1 = np.load(f"infected_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{movement_range_1}.npy")
infected_2 = np.load(f"infected_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{movement_range_2}.npy")
dead_1 = np.load(f"dead_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{movement_range_1}.npy")
dead_2 = np.load(f"dead_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{movement_range_2}.npy")

#plt.plot(time_1,infected_1,c="red",label="infected with (-7,8) movement")
#plt.plot(time_2,infected_2,c="orange",label="infected with (-3,4) movement")
plt.plot(time_1,dead_1,c="black",label=f"deaths with {movement_range_1} movement")
plt.plot(time_2,dead_2,c="brown",label=f"deaths with {movement_range_2} movement")
plt.legend(loc= "upper right",fontsize = "x-large")