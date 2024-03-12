from Node import Node


class BST:

    def __init__(self):
        self.root = None
        self.last_searched_node = None
        self.height = None

    def set_root(self, key):
        self.root = Node(key)

    def insert(self, key):
        if self.root is None:
            self.set_root(key)
        else:
            self.insert_node(self.root, key)

    def insert_node(self, currentNode, key):
        if key <= currentNode.get_key():
            if currentNode.get_left():
                self.insert_node(currentNode.get_left(), key)
            else:
                currentNode.set_left(Node(key))
                currentNode.get_left().set_father(currentNode)
        elif key > currentNode.get_key():
            if currentNode.get_right():
                self.insert_node(currentNode.get_right(), key)
            else:
                currentNode.set_right(Node(key))
                currentNode.get_right().set_father(currentNode)

    def find(self, key):
        return self.find_node(self.root, key)

    def find_node(self, current_node, key):
        if current_node is None:
            return False
        elif key == current_node.get_key():
            self.last_searched_node = current_node
            return True
        elif key < current_node.get_key():
            return self.find_node(current_node.get_left(), key)
        else:
            return self.find_node(current_node.get_right(), key)

    def x_order(self, x="in"):
        self._x_order(self.root, x)

    def _x_order(self, v, x="in"):
        # if v is None:
        #     return "empty"
        if x == "pre":
            v.print()
        if v.get_left() is not None:
            self._x_order(v.get_left(), x)
        if x == "in":
            v.print()
        if v.get_right() is not None:
            self._x_order(v.get_right(), x)
        if x == "post":
            v.print()

    def max_node(self, current_node):
        if current_node is None:
            return False
        while current_node.get_right() is not None:
            current_node = current_node.get_right()
        return current_node.get_key()

    def max(self):
        return self.max_node(self.root)

    def min_node(self, current_node):
        if current_node is None:
            return False
        while current_node.get_left() is not None:
            current_node = current_node.get_left()
        return current_node.get_key()

    def min(self):
        return self.min_node(self.root)

    def get_node(self, key):
        if self.find(key):
            return self.last_searched_node

    def successor(self, key):
        if self.find(key) is False:
            return False
        current_node = self.get_node(key)
        if current_node.get_right() is not None:
            return self.min_node(current_node.get_right())
        current_father = current_node.get_father()
        while current_father is not None and current_node is current_father.get_right():
            current_node = current_father
            current_father = current_node.get_father()
        return current_father.get_key()

    def predecessor(self, key):
        if self.find(key) is False:
            return False
        current_node = self.get_node(key)
        if current_node.get_left() is not None:
            return self.max_node(current_node.get_left())
        current_father = current_node.get_father()
        while current_father is not None and current_node is current_father.get_left():
            current_node = current_father
            current_father = current_node.get_father()
        return current_father.get_key()

    def _graft(self, key_1, key_2):
        node1 = self.get_node(key_1)
        node2 = self.get_node(key_2)
        self.__graft(node1, node2)

    def __graft(self, node1, node2):
        if node1 is not None and node2 is not None:
            if node1.get_father() is None:
                self.root = node2
            elif node1 is node1.get_father().get_left():
                node1.get_father().set_left(node2)
            else:
                node1.get_father().set_right(node2)
            if node2 is not None:
                node2.set_father(node1.get_father())

    def delete(self, key):
        current_node = self.get_node(key)
        if current_node is not None:
            if current_node.get_left() is None:
                self.__graft(current_node, current_node.get_right())
            elif current_node.get_right() is None:
                self.__graft(current_node, current_node.get_left())
            else:
                current_successor = self.get_node(self.min_node(current_node.get_right()))
                if current_successor.get_father() is not current_node:
                    current_successor.get_father().set_left(None)
                    self.__graft(current_successor, current_successor.get_right())
                    current_successor.set_right(current_node.get_right())
                    current_successor.get_right().set_father(current_successor)
                self.__graft(current_node, current_successor)
                current_successor.set_left(current_node.get_left())
                current_successor.get_left().set_father(current_successor)

    def clear(self):
        self.root = None

    def get_height(self):
        self.height = 0
        node = self.root
        self._get_height(node, 0)
        return self.height

    def _get_height(self, node, height):
        if node.get_left():
            self._get_height(node.get_left(), height + 1)
        if node.get_right():
            self._get_height(node.get_right(), height + 1)
        if self.height < height:
            self.height = height
