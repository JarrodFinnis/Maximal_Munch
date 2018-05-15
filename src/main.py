# Maximal Munch Algorithm
# Jarrod Finnis
# 14/05/2018

from src.Tree import Tree
from src.Node import Node


def tree_structure(file):
    line = file.readline()
    tree_temp = Tree(line)
    tree_temp.get_root().set_parent(None)
    node = tree_temp.get_root()
    branch = 0

    for line in file:
        # print(line)
        count = 0
        while line[0] == '=':
            line = line[1:]
            count += 1

        if count == branch:
            branch -= 1
            temp = node
            node = node.get_parent()
            node = node.add_child(Node(line))
            node.set_parent(temp)

        elif count > branch:
            branch += 1
            temp = node
            node = node.add_child(Node(line))
            node.set_parent(temp)

        elif count < branch:
            levels = branch - count
            branch -= levels
            for i in range(levels+1):
                node = node.get_parent()

            temp = node
            node = node.add_child(Node(line))
            node.set_parent(temp)

    return tree_temp


if __name__ == "__main__":
    # f = open(sys.argv[1], "r")
    filename = "testdata2.ir"
    f = open(filename, "r")

    try:
        tree = tree_structure(f)
        representation = ""
        Tree.depth_tree(tree.get_root())
        f.close()
    except IOError as erno:
        print("Could not find the file")
        print("Error number is:", erno)
    finally:
        print("Done")
