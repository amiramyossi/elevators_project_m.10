import pygame
import math
from Floor import Floor
from Lift import Lift
import time

GREEN = (0,255,0)
BLACK = (0, 0, 0)
class Building:

    def __init__(self, screen, floor_amount, lift_amount):

        self.__screen = screen 
        

        self.__floors = []
        for i in range(floor_amount + 1):
            self.__floors.append(Floor(i))
        self.__lifts = []
        for i in range(lift_amount):
            self.__lifts.append(Lift(i + 1))
            self.__lifts[i].set_current_floor(self.__floors[0])
            
      

    def build(self, elapsed_time):



        

        

        for lift in self.__lifts:
            lift.draw_lift(self.__screen)
            lift.manage_tasks()
          
        for floor in self.__floors:
            floor.draw_floor(self.__screen, elapsed_time)   

        


            

    def check_floor_requests(self):
        for floor in self.__floors:
            if floor.need_lift() == "Please send a lift.":
              
                self.call_lift(floor)
                floor.set_need_lift("I'm taken care of.")
                floor.change_colour(GREEN)
                
                

    def check_lift_arrivals(self):
        for lift in self.__lifts:
            if lift.get_arrival_status():
                floor = lift.get_current_floor()
                floor.set_need_lift("No need for a lift.")
                floor.set_colour()
                
               
                    
                


    def get_button_y(self, floor_num):
        return self.__floors[floor_num].get_button_y()            

                   

    def get_floors(self):
        return self.__floors  

    def get_lifts(self):
        return self.__lifts 

 

    def get_best_lift(self, floor):
        minimum_time = float('inf')
        best_lift = None
        for lift in self.__lifts:
            lift_tasks = lift.get_tasks()
            if lift_tasks:
                lift_last_floor, lift_finish_time = lift_tasks[-1] 
            else:
                  lift_last_floor, lift_finish_time = lift.get_current_floor(), time.time() 
            

            potential_finish_time = 2 + lift_finish_time + abs(floor.get_floor_num() - lift_last_floor.get_floor_num()) * 0.5     
            if potential_finish_time < minimum_time:
                best_lift = lift
                minimum_time = potential_finish_time
        return best_lift, minimum_time 


    def call_lift(self, floor):
        best_lift, finish_time = self.get_best_lift(floor)
        
        best_lift.set_tasks(floor, finish_time)
        floor.initialize_timer(finish_time - 2)
      
      
      
      
  


   
              
            











    





           

      






        

