from flask import jsonify
class BinaryFile:
    def __init__(self, fileName, content = None, father = None):
        self.fileName = fileName
        self.content = content
        self.father = father
        self.deleted = False

    def __delete__(self):
        if self.deleted is False:
            self.deleted = True
            return jsonify({'message': self.fileName +' deleted'}), 200
        else: 
            return jsonify({'error': 'File is already deleted'}), 400

    def __move__(self, path):
        if (path.count_elems >= path.DIR_MAX_ELEMS + 1):
            return {'error': 'Target directory is full'}

        self.father = path
        self.father.list.append(self)
        self.father.count_elems += 1 
        return {'message': 'File moved successfully'}

    def __read__(self):
        return {'content': self.content}