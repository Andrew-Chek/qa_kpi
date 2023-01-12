class Directory:
    def __init__(self, name, max_elems, parent = None):
        if parent != None:
            if (parent.count_elems >= parent.DIR_MAX_ELEMS ):
                print('Parent directory is full.')
                return
            parent.count_elems += 1
            parent.list.append(self)
        self.parent = parent
        self.name = name
        self.DIR_MAX_ELEMS = max_elems
        self.count_elems = 0
        self.list = []

    def __delete__(self, instance):
        print('Directory was deleted.')
        return

    def list_elems(self):
        res = self.name + ': ( '
        for item in self.list:
            if type(item) is Directory:
                res += item.list_elems()
            else:
                res += item.name
                res += ', ' 
        res += '), '
        return res

    def move(self, location):
        if (location.count_elems >= location.DIR_MAX_ELEMS + self.count_elems + 1):
            print('Directory is full. Can\'t move.')
            return
        if self.parent != None:
            self.parent.count_elems -= self.count_elems + 1
            index = self.parent.list.index(self)
            self.parent.list.pop(index)
        self.parent = location
        self.parent.list.append(self)
        self.parent.count_elems += self.count_elems + 1 