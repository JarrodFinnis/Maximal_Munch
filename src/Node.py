class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setParent(self, par):
        self.parent = par

    def getParent(self):
        return self.parent

    def addChild(self, child):
        self.children.append(child)
        return child

    def hasChildren(self):
        if (len(self.children) > 0):
            return True
        return False


    def getChildren(self):
        if (self.hasChildren()):
            return self.children
        else:
            return None
