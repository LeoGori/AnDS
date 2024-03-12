from Node import Node

BLACK = "BLACK"
RED = "RED"


class RBNode(Node):

    def __init__(self, key=None):
        Node.__init__(self, key)
        if key is None:
            self.__color = None
        else:
            self._left = RBNode(None)
            self._right = RBNode(None)
            self.__color = RED

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def print(self):
        if self.get_key() is not None:
            print(str(self.get_key()) + ' , ' + self.__color)
