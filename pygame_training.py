import pygame
from Floor import Floor
from Building import Building
from Lift import Lift
import time


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
FLOOR_HEIGHT = 80

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Figuring out this Drek")




# sixth_floor = Floor(6)
# lifty = Lift(1)


BUILDING_HEIGHT = 11
building = Building(screen, BUILDING_HEIGHT, 1)

# clock = pygame.time.Clock()
# clock.tick(60)


running = True
reference_time = time.time()
# iteration = 1
# cycle = 5
while running:
    start = time.time()
    # if cycle == 0:
    current_time = time.time()
    building.update_times(abs(reference_time - current_time))
    reference_time = current_time
    # else:
    #     iteration += 1 % cycle
    
    screen.fill((255, 255, 255))
    building.build()
    building.check_floor_requests()
    building.check_lift_arrivals()
    # dst = building.get_sixth_floor_test()
    # building.get_first_lift_test().move(dst)
    # test_floor = building.get_floors()[3]
    # test_floor.request_lift()
    end = time.time()
    if 1 / 33.42 + start - end > 0:
        time.sleep(1 / 33.42 + start - end)
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
                        
                # building.check_click(mouse_position[1])    

    pygame.display.flip()

pygame.quit()


