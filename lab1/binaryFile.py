class BinaryFile:
    def __init__(self, fileName, content = None, father = None):
        self.file_name = fileName
        self.content = content
        self.father = father
        self.info = content

    def __delete__(self):
        return

    def __move__(self, path):
        return

    def __read__(self):
        return