class Building:

    def __init__(self, floor_amount, lift_amount, screen):

        self.__screen = screen 

        self.__floors = []
        for i in range(floor_amount + 1):
            self.__floors.append(Floor(i))
        self.__lifts = []
        for i in range(lift_amount):
            self.__lifts.append(Lift(i + 1))

    def run():
        pass

    def draw_all():
        pass



    





           

      






        

