# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:39:48 2020

@author: Osama
"""
import random
import environment_variables as env
import time 

size_range=(8,12)
movement_range=(-3,4)
recovery_time = (14,30)

class Blob:

    def __init__(self, isInfected):
        self.size = random.randrange(size_range[0],size_range[1])
        self.isInfected = isInfected
        if(isInfected):
            self.color = env.RED
            self.recoverytime = time.time() + random.randrange(recovery_time[0]-recovery_time[0]//3,recovery_time[1]-recovery_time[0]//3)
        else:
            self.color = env.BLUE
        self.x_boundary = env.WIDTH
        self.y_boundary = env.HEIGHT
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.movement_range = movement_range

    def move(self):
        if self.color == env.BLUE or self.color == env.RED:
            self.move_x = random.randrange(self.movement_range[0],self.movement_range[1])
            self.move_y = random.randrange(self.movement_range[0],self.movement_range[1])
            self.x += self.move_x
            self.y += self.move_y

    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary
        
        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
    
    def recover(self):
        self.color = env.GREEN
        self.infected = False
    
    def __add__(self, other_blob):
        if other_blob.isInfected :
            pass     
        elif not other_blob.isInfected:
            other_blob.isInfected = True
            other_blob.color = env.RED
            other_blob.recoverytime = time.time() + random.randrange(recovery_time[0],recovery_time[1])
            
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors!')