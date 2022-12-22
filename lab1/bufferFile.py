class BufferFile:
    def __init__(self, fileName, maxSize = 0, father = None):
        self.MAX_BUF_FILE_SIZE = maxSize
        self.fileName = fileName
        self.father = father
        self.content = []

    def __delete__(self):
        return

    def __move__(self, path):
        return

    def __push__(self, elem):
        return

    def __consume__(self):
        return