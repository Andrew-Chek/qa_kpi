from flask import Flask, request, jsonify
import json
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

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

app = Flask(__name__)

@app.route('/binaryfile', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def BinaryApi():
    if(request.method == 'GET'):
        return binary.__read__()
    elif(request.method == 'POST'):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        binary = BinaryFile(data["fileName"], data["content"], fatherDir)
        return {'message': 'BinaryFile is successfully created'}
    elif(request.method == 'PUT'):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return binary.__move__(fatherDir)
    elif(request.method == 'DELETE'):
        return binary.__delete__()

@app.route('/bufferfile', methods = ['GET', 'POST', 'PUT', 'PATCH' 'DELETE'])
def BufferApi():
    if(request.method == 'GET'):
        return buffer.__consume__()
    elif(request.method == 'POST'):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        buffer = BufferFile(data["fileName"], data["maxSize"], fatherDir)
        return {'message': 'BufferFile is successfully created'}
    elif(request.method == 'PUT'):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return buffer.__move__(fatherDir)
    elif(request.method == 'PATCH'):
        data = json.loads(request.data)
        return buffer.__push__(data["element"])
    elif(request.method == 'DELETE'):
        return buffer.__delete__()

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