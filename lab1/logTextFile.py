class LogTextFile:
    def __init__(self, fileName, father = None):
        self.fileName = fileName
        self.father = father
        self.content = []

    def __delete__(self):
        return

    def __move__(self, path):
        return

    def __read__(self):
        return

    def __log__(self, newLine):
        return