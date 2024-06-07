import pygame
from collections import deque
import math
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
        self.__stay_input_iterations = 0
        self.__reference = False
        self.__starting_time = 0
        self.__pause_time = 0
        
        
   
       


    def draw_lift(self, screen):
        
        occupied_pixels = ROOM_FOR_TIMER + FLOOR_WIDTH * (self.__num - 1)
        
        screen.blit(self.lift_image, (occupied_pixels, self.__y))

    def set_tasks(self, floor, arrival_time):
        self.__tasks.append((floor, arrival_time)) 

    def update_finish_time(self, passed_time):
        if self.__tasks:
            for i in range(len(self.__tasks)):
                floor, finish_time = self.__tasks[i]
                if finish_time >= passed_time:
                    finish_time -= passed_time
                else:
                    finish_time = 0
                self.__tasks[i] = floor, finish_time        


    def set_current_floor(self, floor):
        self.__current_floor = floor

    def get_current_floor(self):
        return self.__current_floor
    
    def get_arrival_status(self):
        return self.__arrival_status
    
    def set_arrival_status(self, status=bool):
        self.__arrival_status = status

    def get_pause_time(self):
        return self.__pause_time    
    

    def move(self, dst):
        self.__current_floor = dst 
        
        y_of_dst = dst.get_y() 
        if self.__y != y_of_dst:
            self.set_arrival_status(False)
            if self.__y < y_of_dst:
                self.__y += 5
            else:
                self.__y -= 5       
        
        else:
            
            
            if not self.__reference:
                self.set_arrival_status(True)
                self.__starting_time = time.time()
                pygame.mixer.Sound.play(ding)
                self.__reference = True
                
                 
                
                
                

            else:
                
                two_sec_check = time.time()
                if two_sec_check - self.__starting_time > 2:
                    
                 
                    self.__reference = False
                    self.__tasks.popleft()
                    
                    self.__starting_time = 0

                # else:{}
                    
               
            
           


        
         

    


    def get_tasks(self):
        return self.__tasks            

    def manage_tasks(self):
        if self.__tasks:
            dst, _ = self.__tasks[0]
            self.move(dst)
        
                        

  



    