class Clickable:
    def __init__(self, pos):
        self.__range_x = (pos[0][0], pos[1][0])
        self.__range_y = (pos[0][1], pos[1][1])
        
    def in_range(self, pos):
        if (self.__range_x[0] <= pos[0] <= self.__range_x[1]) and (self.__range_y[0] <= pos[1] <= self.__range_y[1]):
            return True
        return False