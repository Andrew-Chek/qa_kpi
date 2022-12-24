class Directory:
    def __init__(self, dirName, maxElements = 0, father = None):
        self.DIR_MAX_ELEMS = maxElements
        self.father = father
        self.name = dirName
        self.elementsCount = 0
        self.fileList = []

    def __delete__(self):
        return {'message': self.name +'directory deleted'}

    def __listElements__(self):
        answ = ''
        for item in self.fileList:
            if type(item) is Directory:
                answ += '==='
                answ += item.__listElements__()
                answ += '==='

            else:
                answ += item.name
                answ += ', ' 

        return answ

    def __move__(self, path):
        if (path.elementsCount >= path.DIR_MAX_ELEMS + 1):
            return {'error': 'Target directory is full'}

        if self.father != None:
            self.father.elementsCount -= 1
            self.father.fileList.pop(self.father.fileList.index(self))

        self.father = path
        self.father.fileList.append(self)
        self.father.elementsCount += 1 
        return {'message': 'Directory moved successfully'}