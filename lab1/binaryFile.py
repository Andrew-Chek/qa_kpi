class BinaryFile:
    def __init__(self, fileName, content = None, father = None):
        self.fileName = fileName
        self.content = content
        self.father = father
        self.info = content

    def __delete__(self):
        print(self.fileName +'file deleted')
        return

    def __move__(self, path):
        if (path.elementsCount >= path.DIR_MAX_ELEMS + 1):
            print('Target directory is full')
            return

        if self.father != None:
            self.father.elementsCount -= 1
            self.father.fileList.pop(self.father.fileList.index(self))

        self.father = path
        self.father.fileList.append(self)
        self.father.elementsCount += 1 
        return

    def __read__(self):
        return self.content