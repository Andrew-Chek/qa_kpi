class Directory:
    def __init__(self, dirName, maxElements, father):
        self.DIR_MAX_ELEMS = maxElements
        self.father = father
        self.name = dirName
        self.elementsCount = 0
        self.fileList = []

    def delete(self):
        return

    def listElements(self):
        return

    def move(self, path):
        return