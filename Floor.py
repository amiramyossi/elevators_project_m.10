import pygame
from Lift import Lift

SCREEN_HEIGHT = 1000
FLOOR_HEIGHT = 80
FLOOR_WIDTH = 100
GREEN = (0,255,0)
BLACK = (0, 0, 0)
NICE_GREY = (119,136,153)
class Floor:

    def __init__(self, num):
        self.__num = num
          
        self.__ceiling = FLOOR_HEIGHT * (self.__num + 1)
        self.__button_y = 0
        self.__need_lift = "No need for a lift."
        self.__timer = 0
        self.__iterations = 0
        self.__num_colour = BLACK


    def draw_floor(self, screen):
        occupied_pixels = FLOOR_HEIGHT * (self.__num)
        floor_image_big = pygame.image.load("floor_image.jpeg").convert_alpha()
        floor_image = pygame.transform.scale(floor_image_big, (FLOOR_WIDTH, FLOOR_HEIGHT))
        rect_area = pygame.Rect(0, 0, FLOOR_WIDTH, FLOOR_HEIGHT)
        rect_area.bottomleft = (0, SCREEN_HEIGHT - occupied_pixels)
        screen.blit(floor_image, rect_area)
        black_line = pygame.Rect(rect_area.topleft[0], rect_area.topleft[1], FLOOR_WIDTH, 7)
        pygame.draw.rect(screen, (0, 0, 0), black_line)
        button = pygame.Rect(0, 0, 25, 25)
        button.center = rect_area.center
        pygame.draw.rect(screen, NICE_GREY, (button.topleft[0] - 5, button.topleft[1], 30, 30), border_radius=8)
        self.__button_y = button.topleft[1]
        font = pygame.font.SysFont(None, 30)
        screen.blit(font.render(str(self.__num), True, self.__num_colour), font.render(str(self.__num), True, (255, 0, 0)).get_rect(center=(rect_area.center[0] - 2, rect_area.center[1] + 3)))
        timer_font = pygame.font.SysFont(None, 30)
        if self.__timer > 0:
           display_time = round(self.__timer * 2) / 2  # Round to the nearest 0.5
           screen.blit(timer_font.render(str(display_time), True, (0, 0, 0)), timer_font.render(str(display_time), True, (255, 0, 0)).get_rect(center=(rect_area.center[0] + 80, rect_area.center[1] + 3)))




    def request_lift(self):
        if self.__need_lift == "No need for a lift.":
            self.__need_lift = "Please send a lift."
            self.__num_colour = GREEN 
        else:
            return    

               

    def need_lift(self):
        return self.__need_lift
    
    def set_need_lift(self, str):
        self.__need_lift = str

    def set_colour(self):
        self.__num_colour = BLACK  

    def initialize_timer(self, time):
        self.__iterations = 1
        self.__timer = time  


    def update_timer(self, elapsed_time):
        if self.__timer > 0:
            self.__timer = max(0, self.__timer - elapsed_time)      
        

    # def update_timer(self):
    #     if self.__iterations < 16:
    #         self.__iterations += 1
    #     elif self.__timer >= 0.5:
    #         self.__timer -= 0.5
    #         self.__iterations = 0
    #     else:
    #         self.__iterations = 0        
    

    def change_colour(self, colour):
        self.__num_colour = colour
              

    def get_button_y(self):
        return self.__button_y    

    def get_floor_num(self):
        return self.__num    

    def display_time(self, arrival_time):
        pass

    def ding():
        pass

    def change_colour(self, to_colour):
        pass    

    def get_y(self):
        return SCREEN_HEIGHT - self.__ceiling
    
    