import pygame
from Floor import Floor
from Lift import Lift
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
      

    def build(self):
        for floor in self.__floors:
            floor.draw_floor(self.__screen)

        for lift in self.__lifts:
            lift.draw_lift(self.__screen)
            lift.manage_tasks()
         


            

    def check_floor_requests(self):
        for floor in self.__floors:
            if floor.need_lift():
                self.call_lift(floor)

    def check_lift_arrivals(self):
        for lift in self.__lifts:
            if lift.get_arrival_status():
                lift.set_arrival_status(False)
                self.arrive_at_dst(lift, lift.get_current_floor())

    def arrive_at_dst(self, lift, floor):
        floor.update_time_to_wait("")

    # colour, ding, sleep 2 sec, erase timer if needed                     
                


    def get_button_y(self, floor_num):
        return self.__floors[floor_num].get_button_y()            

    # def check_click(self, mouse_click_y):
    #     for floor in self.__floors:
    #         floor.                    

    def get_floors(self):
        return self.__floors   

 

    def get_best_lift(self, floor):
        minimum_time = float('inf')
        best_lift = None
        for lift in self.__lifts:
            lift_tasks = lift.get_tasks()
            if lift_tasks:
                lift_last_floor, lift_finnish_time = lift_tasks[-1]
            else:
                  lift_last_floor, lift_finnish_time = lift.get_current_floor(), 0  
            if lift_finnish_time + abs(floor.get_floor_num() - lift_last_floor.get_floor_num()) / 2 < minimum_time:
                minimum_time = lift_finnish_time + abs(floor.get_floor_num() - lift_last_floor.get_floor_num()) / 2
                best_lift = lift
        return best_lift, minimum_time 


    def call_lift(self, floor):
        best_lift, arrival_time = self.get_best_lift(floor)
        if len(best_lift.get_tasks()) < 1:
            best_lift.set_tasks(floor, arrival_time)
        else:
            best_lift.set_tasks(floor, arrival_time + 2)   
        floor.set_need_lift()
        # display_time(arrival_time)
        # change_colour(to_green)

    def update_times(self, passed_time):
        for lift in self.__lifts:
            lift.update_finish_time(passed_time)
            if lift.get_tasks():
                for i in range(len(lift.get_tasks())):
                    floor, arrival_time = lift.get_tasks()[i]
                    floor.update_time_to_wait(int(arrival_time))
            











    





           

      






        

