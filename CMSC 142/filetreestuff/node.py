import datetime as dt

class Node:
    def __init__(self, node_name:str, parent_node: Node=None):
        self.name: str = node_name
        self.parentNode: Node = parent_node
        self.childNodes: [Node] = []
        self.dateCreated = dt.datetime.now()
        self.changeHistory = []

    def getName(self) -> str:
        return self.name

    def getParentName(self) -> str:
        return self.parentNode.getName()

    def getChildNodes(self) -> [Node]:
        return self.childNodes

    def rename(self, new_name: str):
        self.name = new_name
        self.changeHistory.append(dt.datetime.now())

    def childUpdate()

    def updateParentHistory()
