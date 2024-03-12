from BST import BST
from RBNode import RBNode

RED = 'RED'
BLACK = 'BLACK'


class RBT(BST):

    def __init__(self):
        BST.__init__(self)

    def set_root(self, node):
        self.root = node
        self.root.set_father(RBNode())

    def left_rotate(self, current_node):
        #if current_node.get_right() is not None:
        current_right = current_node.get_right()
        current_node.set_right(current_right.get_left())
        if current_right.get_left().get_key() is not None:
            current_right.get_left().set_father(current_node)
        current_right.set_father(current_node.get_father())
        if current_node.get_father().get_key() is None:
            self.root = current_right
        elif current_node is current_node.get_father().get_left():
            current_node.get_father().set_left(current_right)
        else:
            current_node.get_father().set_right(current_right)
        current_right.set_left(current_node)
        current_node.set_father(current_right)

    def right_rotate(self, current_node):
        #if current_node.get_left() is not None:
        current_left = current_node.get_left()
        current_node.set_left(current_left.get_right())
        if current_left.get_right().get_key() is not None:
            current_left.get_right().set_father(current_node)
        current_left.set_father(current_node.get_father())
        if current_node.get_father().get_key() is None:
            self.root = current_left
        elif current_node is current_node.get_father().get_right():
            current_node.get_father().set_right(current_left)
        else:
            current_node.get_father().set_left(current_left)
        current_left.set_right(current_node)
        current_node.set_father(current_left)

    def insert(self, key):
        node = RBNode(key)
        if self.root is None:
            self.set_root(node)
        else:
            self.insert_node(self.root, node)

        self._rb_insert_fix_up(node)

    def insert_node(self, current_node, node_to_insert):
        if node_to_insert.get_key() <= current_node.get_key():
            if current_node.get_left().get_key() is not None:
                self.insert_node(current_node.get_left(), node_to_insert)
            else:
                current_node.set_left(node_to_insert)
                node_to_insert.set_father(current_node)
        elif node_to_insert.get_key() > current_node.get_key():
            if current_node.get_right().get_key() is not None:
                self.insert_node(current_node.get_right(), node_to_insert)
            else:
                current_node.set_right(node_to_insert)
                node_to_insert.set_father(current_node)

    def _rb_insert_fix_up(self, node):
        while node.get_father().get_color() == RED:
            node_father = node.get_father()
            node_grandfather = node_father.get_father()
            if node_father is node_grandfather.get_left():
                node_uncle = node_grandfather.get_right()
                if node_uncle.get_color() == RED:
                    node_father.set_color(BLACK)
                    node_uncle.set_color(BLACK)
                    node_grandfather.set_color(RED)
                    node = node_grandfather
                else:
                    if node is node_father.get_right():
                        node = node_father
                        self.left_rotate(node)
                    node_father.set_color(BLACK)
                    node_grandfather.set_color(RED)
                    self.right_rotate(node_grandfather)
            elif node_father is node_grandfather.get_right():
                node_uncle = node_grandfather.get_left()
                if node_uncle.get_color() == RED:
                    node_father.set_color(BLACK)
                    node_uncle.set_color(BLACK)
                    node_grandfather.set_color(RED)
                    node = node_grandfather
                else:
                    if node is node_father.get_left():
                        node = node_father
                        self.right_rotate(node)
                    node_father.set_color(BLACK)
                    node_grandfather.set_color(RED)
                    self.left_rotate(node_grandfather)

            self.root.set_color(BLACK)

    def get_height(self):
        return super().get_height() - 1
