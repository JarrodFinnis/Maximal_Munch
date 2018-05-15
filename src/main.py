# Maximal Munch Algorithm
# Jarrod Finnis
# 14/05/2018

import sys
from src.Tree import Tree
from src.Node import Node

def treeStructure(file):
    line = file.readline()
    treeTemp = Tree(line)
    node = treeTemp.root
    branch = 0

    for line in file:
        count = 0
        while (line[0] == '='):
            line = line[1:]
            count += 1

        if (count > branch):
            temp = node
            node = node.addChild(Node(line))
            node.setParent(temp)
            branch += 1

        elif (count < branch):
            levels = branch - count
            branch -= levels
            for i in range(levels):
                node = node.getParent()

            temp = node
            node = node.addChild(Node(line))
            node.setParent(temp)

    return treeTemp


if __name__ == "__main__":
    #f = open(sys.argv[1], "r")
    filename = "testdata1.ir"
    f = open(filename, "r")

    try:
        tree = treeStructure(f)
        tree.depthTree(tree.getRoot())
        f.close()
    except IOError as erno:
        print("Could not find the file")
        print("Error number is:", erno)
    finally:
        print("Done")