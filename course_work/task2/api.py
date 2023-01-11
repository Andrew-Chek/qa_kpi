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

@app.route('/bufferfile', methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
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

@app.route('/directory', methods = ['POST', 'PUT', 'DELETE'])
def DirectoryApi():
    if(request.method == 'POST'):
        data = request.get_json()
        directory = Directory(data["name"], data["maxElements"])
        return {'message': 'Directory is successfully created'}
    elif(request.method == 'PUT'):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return directory.__move__(fatherDir)
    elif(request.method == 'DELETE'):
        return directory.__delete__()

@app.route('/logtext', methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def logTextApi():
    if(request.method == 'GET'):
        return logText.__read__()
    if(request.method == 'POST'):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        logText = LogTextFile(data["fileName"], fatherDir)
        return {'message': 'LogTextFile is successfully created'}
    if(request.method == 'PUT'):
        data = request.get_json()
        fatherDir = Directory(data["father"])
        return logText.__move__(fatherDir)
    if(request.method == 'PATCH'):
        data = request.get_json()
        return logText.__log__(data["line"])
    if(request.method == 'DELETE'):
        return logText.__delete__()

if __name__ == '__main__':
    app.run(debug=True)