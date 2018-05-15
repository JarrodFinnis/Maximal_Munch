# Nodes that make up the tree structure


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_parent(self, par):
        self.parent = par

    def get_parent(self):
        return self.parent

    def add_child(self, child):
        self.children.append(child)
        return child

    def has_children(self):
        if len(self.children) > 0:
            return True
        return False

    def get_children(self):
        if self.has_children():
            return self.children
        else:
            return None
