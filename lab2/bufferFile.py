class BufferFile:
    def __init__(self, fileName, maxSize = 0, father = None):
        self.MAX_BUF_FILE_SIZE = maxSize
        self.fileName = fileName
        self.father = father
        self.content = []
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

    def __push__(self, elem):
        if len(self.content) >= self.MAX_BUF_FILE_SIZE:
            return {'error': 'Buffer is full'}

        self.content.append(elem)
        return {'content': self.content}

    def __consume__(self):
        if len(self.content) >= 1:
            temp = self.content[0]
            self.content.pop(0)
            return {'consumed content': temp}
        return {'error': 'content is empty'}