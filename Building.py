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
        self.__last_update_time = time.time()

        self.__floors = []
        for i in range(floor_amount + 1):
            self.__floors.append(Floor(i))
        self.__lifts = []
        for i in range(lift_amount):
            self.__lifts.append(Lift(i + 1))
            self.__lifts[i].set_current_floor(self.__floors[0])
            # sel.__test_flip = True
      

    def build(self):
        for floor in self.__floors:
            floor.draw_floor(self.__screen)

        

        for lift in self.__lifts:
            lift.draw_lift(self.__screen)
            lift.manage_tasks()
         


            

    def check_floor_requests(self):
        for floor in self.__floors:
            if floor.need_lift() == "Please send a lift.":
                # for lift in self.__lifts:
                #     if lift.get_current_floor() == floor:
                #         floor.set_need_lift()
                #         return None
                self.call_lift(floor)
                floor.set_need_lift("I'm taken care of.")
                floor.change_colour(GREEN)
                
                

    def check_lift_arrivals(self):
        for lift in self.__lifts:
            if lift.get_arrival_status():
                floor = lift.get_current_floor()
                floor.set_need_lift("No need for a lift.")
                floor.set_colour()
                
                self.arrive_at_dst(lift, lift.get_current_floor())
                # lift.set_arrival_status(False)

    def arrive_at_dst(self, lift, floor):
        # floor.update_time_to_wait(0)
        floor.change_colour(BLACK)
        
        

    # colour, ding, sleep 2 sec, erase timer if needed                     
                


    def get_button_y(self, floor_num):
        return self.__floors[floor_num].get_button_y()            

    # def check_click(self, mouse_click_y):
    #     for floor in self.__floors:
    #         floor.                    

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
                  lift_last_floor, lift_finish_time = lift.get_current_floor(), 0 
            if lift.get_arrival_status():
                remaining_wait_time = max(0, 2 - lift.get_pause_time())
            else:
                remaining_wait_time = 0

            arrival_time = lift_finish_time + remaining_wait_time + abs(floor.get_floor_num() - lift_last_floor.get_floor_num()) * 0.5     
            if arrival_time < minimum_time:
                best_lift = lift
                minimum_time = arrival_time
        return best_lift, minimum_time 


    def call_lift(self, floor):
        best_lift, arrival_time = self.get_best_lift(floor)
        remaining_wait_time = max(0, 2 - best_lift.get_pause_time()) if best_lift.get_arrival_status() else 0
       
        if len(best_lift.get_tasks()) > 1 and best_lift.get_arrival_status():
            best_lift.set_tasks(floor, arrival_time + remaining_wait_time)
            floor.initialize_timer(arrival_time + remaining_wait_time)
        elif best_lift.get_tasks() and not best_lift.get_arrival_status():
            best_lift.set_tasks(floor, arrival_time + 2)
            floor.initialize_timer(arrival_time + 2)
        else:
            best_lift.set_tasks(floor, arrival_time)
            floor.initialize_timer(arrival_time)  
      
      
      
      
        # if len(best_lift.get_tasks()) > 1:
        #     best_lift.set_tasks(floor, arrival_time + 2)
        #     floor.initialize_timer(arrival_time + 2)
        # elif len(best_lift.get_tasks()) == 1 and not best_lift.get_arrival_status():
        #     best_lift.set_tasks(floor, arrival_time + 2)
        #     floor.initialize_timer(arrival_time + 2)   
        # else:
        #     best_lift.set_tasks(floor, arrival_time)
        #     floor.initialize_timer(arrival_time)  
        

    # def update_times(self):
    #     for lift in self.__lifts:
    #          if lift.get_tasks():
    #             lift.update_finish_time()
    #     for floor in self.__floors:
    #         floor.update_timer()       
            

    def update_times(self):
        current_time = time.time()
        elapsed_time = current_time - self.__last_update_time
        self.__last_update_time = current_time

        for lift in self.__lifts:
            if lift.get_tasks():
                lift.update_finish_time(elapsed_time)
        for floor in self.__floors:
            floor.update_timer(elapsed_time)
  

              
            











    





           

      






        

