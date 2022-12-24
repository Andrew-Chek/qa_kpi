from flask import Flask, request
import json
from flask_restful import Resource, Api
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

app = Flask(__name__)
api = Api(app)

fatherDirectory = Directory('fatherDir')

fileName = 'binary file'
content = 'binary content'
binary = BinaryFile(fileName, content, fatherDirectory)

name = 'buffer file'
size = 10
buffer = BufferFile(name, size)

maxElements = 10
name = 'name1'
directory = Directory(name, maxElements)

name = 'name1'
log = LogTextFile(name, fatherDirectory)

class BinaryApi(Resource):
    def __init__(self):
        self.binary = binary
    def get(self):
        return self.binary.__read__()
    def post(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        self.binary = BinaryFile(data["fileName"], data["content"], fatherDir)
        return {'message': 'BinaryFile is successfully created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.binary.__move__(fatherDir)
    def delete(self):
        return self.binary.__delete__()

class BufferApi(Resource):
    def __init__(self):
        self.buffer = buffer
    def get(self):
        return self.buffer.__consume__()
    def post(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        self.buffer = BufferFile(data["fileName"], data["maxSize"], fatherDir)
        return {'message': 'BufferFile is successfully created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.buffer.__move__(fatherDir)
    def patch(self):
        data = json.loads(request.data)
        return self.buffer.__push__(data["element"])
    def delete(self):
        return self.buffer.__delete__()

class DirectoryApi(Resource):
    def __init__(self):
        self.directory = directory
    def post(self):
        data = request.get_json()
        self.directory = Directory(data["name"], data["maxElements"])
        return {'message': 'Directory is successfully created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.directory.__move__(fatherDir)
    def delete(self):
        return self.directory.__delete__()

class logTextApi(Resource):
    def __init__(self):
        self.logText = LogTextFile
    def get(self):
        return self.logText.__read__()
    def post(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        self.logText = LogTextFile(data["fileName"], fatherDir)
        return {'message': 'LogTextFile is successfully created'}
    def put(self):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return self.logText.__move__(fatherDir)
    def patch(self):
        data = request.get_json()
        return self.logText.__log__(data["line"])
    def delete(self):
        return self.logText.__delete__()

api.add_resource(BinaryApi, '/binaryfile')
api.add_resource(BufferApi, '/bufferfile')
api.add_resource(DirectoryApi, '/directory')
api.add_resource(logTextApi, '/logtextfile')

if __name__ == '__main__':
    app.run(debug=True)