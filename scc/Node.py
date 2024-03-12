class Node:
    def __init__(self):
        self.__father = None
        self.__f = None
        self.__d = None
        self.__color = None

    def print(self):
        print('id: ' + str(self) + ', padre: ' + str(self.__father) + ', tempo di scoperta: ' + str(self.__d) + ', tempo di fine: ' + str(self.__f))

    def set_f(self, f):
        self.__f = f

    def set_d(self, d):
        self.__d = d

    def set_father(self, father):
        self.__father = father

    def set_color(self, color):
        self.__color = color

    def get_f(self):
        return self.__f

    def get_d(self):
        return self.__d

    def get_father(self):
        return self.__father

    def get_color(self):
        return self.__color

    def reset(self):
        self.__father = None
        self.__f = None
        self.__d = None
        self.__color = None
