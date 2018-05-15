# Tree structure for the files being read-in

from src.Node import Node


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    @staticmethod
    def depth_tree(node):
        if node is not None:
            if node.has_children():
                Tree.depth_tree(node.get_children()[0])

            print(node.get_value(), end="")

            if node.has_children():
                if len(node.get_children()) > 1:
                    for child in node.get_children()[1:]:
                        Tree.depth_tree(child)
