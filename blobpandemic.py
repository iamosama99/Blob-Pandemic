# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:22:23 2020

@author: Osama
"""

import pygame
import random
import math
import blob
from blob import Blob
import numpy as np
import environment_variables as env
import matplotlib.pyplot as plt
import time as tym

STARTING_TOTAL_BLOBS = 200
STARTING_INFECTED_BLOBS = 3
HEALTHCARE_CAPACITY = 40


time = []
total_infected = []
infected_atm = []
recovered = []
dead = []

game_display = pygame.display.set_mode((env.WIDTH, env.HEIGHT))
pygame.display.set_caption("Blob pandemic")
clock = pygame.time.Clock()

def save_lists():
    np.save(f"time_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{blob.movement_range}.npy",time)
    np.save(f"infected_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{blob.movement_range}.npy",infected_atm)
    np.save(f"dead_{STARTING_TOTAL_BLOBS}-{STARTING_INFECTED_BLOBS}-{HEALTHCARE_CAPACITY}-{blob.movement_range}.npy",dead)

def insert_data(reds, blues, green, blacks):   
    time.append(pygame.time.get_ticks()); total_infected.append(len(reds)+len(green)+len(blacks));
    infected_atm.append(len(reds)); recovered.append(len(green)); dead.append(len(blacks))
                   
def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)

def can_survive(reds):
    if(len(reds)<HEALTHCARE_CAPACITY and 40<random.randrange(0,100)<61):
        return False
    elif(len(reds)>HEALTHCARE_CAPACITY and 5<random.randrange(0,20)<15):
        return False
    return True

def handle_collisions(blob_list):
    reds, blues , green, blacks = blob_list
    for red_blob in reds.copy():
        if(math.floor(tym.time())%3==0):
            print(len(reds))
            insert_data(reds, blues , green, blacks)
        if( tym.time() > red_blob.recoverytime ):
            if(not can_survive(reds)):
                red_blob.color = env.BLACK
                blacks.add(red_blob)
                reds.discard(red_blob)
            else:
                red_blob.recover()
                green.add(red_blob)
                reds.discard(red_blob)
            if(len(reds)==0):
                   plot_graph()
                   save_lists()
        for blue_blob in blues.copy():
            if(math.floor(tym.time())%3==0):
                insert_data(reds, blues , green, blacks)
            if(is_touching(red_blob,blue_blob)):
               red_blob+blue_blob
               reds.add(blue_blob)
               blues.discard(blue_blob) 
               if(len(reds)==0):
                   plot_graph()
                   
    return reds, blues , green

def draw_environment(blob_list):
    game_display.fill(env.WHITE)
    reds, blues , green = handle_collisions(blob_list)
    for blob_set in blob_list[0:2]:
        for blob in blob_set:
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()
    return blues, reds

def plot_graph():
    plt.plot(time,total_infected,c="red",label = "total infected")
    plt.plot(time,infected_atm,c="orange", label = "currently infected")
    plt.plot(time,recovered,c="green",label = "recovered")
    plt.plot(time,dead,c="black", label = "deaths")
    plt.xlabel('Blobs',fontsize = 14)
    plt.ylabel('Time',fontsize = 14)
    plt.legend(loc= "upper left",fontsize = "x-large")
    plt.show()
    
def main():
    infected_blobs = set([Blob(True) for i in range(STARTING_INFECTED_BLOBS)])
    normal_blobs = set([Blob(False) for i in range(STARTING_TOTAL_BLOBS - STARTING_INFECTED_BLOBS)])
    RECOVERED = set()
    DEAD = set()
    insert_data(infected_blobs,normal_blobs,RECOVERED,DEAD)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        blue_blobs, red_blobs = draw_environment([infected_blobs,normal_blobs,RECOVERED,DEAD])
        clock.tick(60)

if __name__ == '__main__':
    main()