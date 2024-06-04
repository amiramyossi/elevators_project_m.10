import pygame
from collections import deque
import math


SCREEN_HEIGHT = 1000
FLOOR_HEIGHT = 80
FLOOR_WIDTH = 100
ROOM_FOR_TIMER = 150

class Lift:

    def __init__(self, num):
        self.__current_floor = None
        self.__num = num
        self.__tasks = deque([])
        self.__y = SCREEN_HEIGHT - FLOOR_HEIGHT
        self.lift_image = pygame.image.load("elv.png").convert_alpha()
        self.lift_image = pygame.transform.scale(self.lift_image, (100, 80))
   
       


    def draw_lift(self, screen):
        
        occupied_pixels = ROOM_FOR_TIMER + FLOOR_WIDTH * (self.__num - 1)
        
        screen.blit(self.lift_image, (occupied_pixels, self.__y))

    def set_tasks(self, floor, arrival_time):
        self.__tasks.append((floor, arrival_time)) 

    def update_finish_time(self, passed_time):
        if self.__tasks:
            floor, finish_time = self.__tasks[-1]
            if finish_time >= passed_time:
                finish_time -= passed_time
            else:
                finish_time = 0
            self.__tasks[-1] = floor, finish_time        


    def set_current_floor(self, floor):
        self.__current_floor = floor

    def get_current_floor(self):
        return self.__current_floor
    

    def move(self, dst): 
        self.set_current_floor(dst)
        y_of_dst = dst.get_y() 
        if self.__y != y_of_dst:
            if self.__y < y_of_dst:
                self.__y += 5
            else:
                self.__y -= 5
        
        elif self.__tasks:
            self.__tasks.popleft()
         

    


    def get_tasks(self):
        return self.__tasks            

    def manage_tasks(self):
        if self.__tasks:
            dst, _ = self.__tasks[0]
            self.move(dst)        

  



    