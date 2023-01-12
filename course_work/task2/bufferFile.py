from flask import jsonify
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
            return jsonify({'message': self.fileName +'file deleted'}), 200
        else: 
            return jsonify({'error': 'File is already deleted'}), 400

    def __move__(self, path):
        if (path.elementsCount >= path.DIR_MAX_ELEMS + 1):
            return jsonify({'error': 'Target directory is full'}), 400

        if self.father != None:
            self.father.elementsCount -= 1
            self.father.fileList.pop(self.father.fileList.index(self))

        self.father = path
        self.father.fileList.append(self)
        self.father.elementsCount += 1 
        return jsonify({'message': 'File moved successfully'}), 200

    def __push__(self, elem):
        if len(self.content) >= self.MAX_BUF_FILE_SIZE:
            return jsonify({'error': 'Buffer is full'}), 400

        self.content.append(elem)
        return jsonify({'content': self.content}), 200

    def __consume__(self):
        if len(self.content) >= 1:
            temp = self.content[0]
            self.content.pop(0)
            return jsonify({'consumed content': temp}), 200
        return jsonify({'error': 'content is empty'}), 400