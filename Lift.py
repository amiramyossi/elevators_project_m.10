import pygame
from collections import deque

import time


SCREEN_HEIGHT = 1000
FLOOR_HEIGHT = 80
FLOOR_WIDTH = 100
ROOM_FOR_TIMER = 150

pygame.mixer.init()
ding = pygame.mixer.Sound("ding.mp3")

class Lift:

    def __init__(self, num):
        self.__current_floor = None
        self.__num = num
        self.__tasks = deque([])
        self.__y = SCREEN_HEIGHT - FLOOR_HEIGHT
        self.lift_image = pygame.image.load("elv.png").convert_alpha()
        self.lift_image = pygame.transform.scale(self.lift_image, (100, 80))
        self.__arrival_status = False
        
        self.__waiting = False
        
        
        self.__pause_iterations_left = 0
        
        
        
        
   
       


    def draw_lift(self, screen):
        
        occupied_pixels = ROOM_FOR_TIMER + FLOOR_WIDTH * (self.__num - 1)
        
        screen.blit(self.lift_image, (occupied_pixels, self.__y))

    def set_tasks(self, floor, arrival_time):
       
       
        self.__tasks.append((floor, arrival_time))   

        


    def set_current_floor(self, floor):
        self.__current_floor = floor

    def get_current_floor(self):
        return self.__current_floor
    
    def get_arrival_status(self):
        return self.__arrival_status
    
    def set_arrival_status(self, status=bool):
        self.__arrival_status = status

    def get_pause_time(self):
          
        return (64 - self.__pause_iterations_left) / 32
    

    def move(self, dst, desired_arrival_time):
        
        self.__current_floor = dst 
        
        y_of_dst = dst.get_y()

        time_to_dst = desired_arrival_time - time.time() if desired_arrival_time > time.time() else 0

        if y_of_dst != self.__y:
            self.__arrival_status = False


        if y_of_dst > self.__y:
            self.__y = y_of_dst - (time_to_dst * 160) 

        elif y_of_dst < self.__y:
            self.__y = y_of_dst + (time_to_dst * 160) 

        elif not self.__waiting:
            self.__arrival_status = True      
            pygame.mixer.Sound.play(ding)
            self.__waiting = True

        elif time.time() >= desired_arrival_time + 2:

            self.__waiting = False
                    
            self.__tasks.popleft()
            self.__arrival_status = False
        
           


                
                    
               
            
           


        
         

    


    def get_tasks(self):
        return self.__tasks            

    def manage_tasks(self):
        if self.__tasks:
            dst, finish_time = self.__tasks[0]
            self.move(dst, finish_time - 2)
            
        
                        

  



    