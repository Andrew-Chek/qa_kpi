class BinaryFile:
    def __init__(self, fileName, content = None, father = None):
        self.fileName = fileName
        self.content = content
        self.father = father
        self.info = content
        self.deleted = False

    def __delete__(self):
        if self.deleted is False:
            self.deleted = True
            return {'message': self.fileName +'file deleted'}
        else: 
            return {'error': 'File is already deleted'}

    def __move__(self, path):
        if (path.elementsCount >= path.DIR_MAX_ELEMS + 1):
            return {'error': 'Target directory is full'}

        if self.father != None:
            self.father.elementsCount -= 1
            self.father.fileList.pop(self.father.fileList.index(self))

        self.father = path
        self.father.fileList.append(self)
        self.father.elementsCount += 1 
        return {'message': 'File moved successfully'}

    def __read__(self):
        return {'content': self.content}