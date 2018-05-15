# Tree structure for the files being read in

from src.Node import Node

class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def getRoot(self):
        return self.root

    def depthTree(self, node):
        if (node != None):
            if (node.hasChildren()):
                self.depthTree(node.getChildren()[0])
            print(node.getValue(), end=" ")

            if (node.hasChildren()):
                if (len(node.getChildren()) > 1):
                    for child in node.getChildren()[1:]:
                        self.depthTree(child)