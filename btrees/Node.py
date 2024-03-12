class Node:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._father = None

    def get_key(self):
        return self._key

    def set_key(self, key):
        self._key = key

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_father(self):
        return self._father

    def set_father(self, node):
        self._father = node

    def set_right(self, node):
        self._right = node

    def set_left(self, node):
        self._left = node

    def print(self):
        print(self._key)
