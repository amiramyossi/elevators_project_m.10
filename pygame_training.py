import pygame

from Building import Building

import time


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
FLOOR_HEIGHT = 80

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lift Game")





BUILDING_HEIGHT = 11
building = Building(screen, BUILDING_HEIGHT, 5)




running = True


elapsed_time = 0
start = time.time()
while running:
    
 
           

    
    screen.fill((255, 255, 255))
    

    building.build(elapsed_time)
    building.check_floor_requests()
    building.check_lift_arrivals()

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if mouse_position[0] >= 35 and mouse_position[0] <= 65:
                if mouse_position[1] >= SCREEN_HEIGHT - (FLOOR_HEIGHT * (BUILDING_HEIGHT + 1)):
                    requested_floor = (SCREEN_HEIGHT - mouse_position[1]) // FLOOR_HEIGHT
                    button_y = building.get_button_y(requested_floor)
                    if mouse_position[1] >= button_y and mouse_position[1] <= (button_y + 30):
                        approved_floor = building.get_floors()[requested_floor]
                        clicked = True
                        for lift in building.get_lifts():
                            if lift.get_current_floor() == approved_floor:
                                clicked = False
                                break
                        if clicked:    
                            approved_floor.request_lift()
                        
    end = time.time()
    elapsed_time = end - start
    start = end            

    pygame.display.flip()
    

pygame.quit()


