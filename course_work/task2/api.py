
# @app.route('/bufferfile', methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def BufferApi():
#     if(request.method == 'GET'):
#         status = 200
#         if(buffer.__consume__()["error"] != ""):
#             status = 400
#         return jsonify(buffer.__consume__()), status
#     elif(request.method == 'POST'):
#         fatherDir = Directory(request.args.get("father"))
#         buffer = BufferFile(request.args.get("fileName"), request.args.get("maxSize"), fatherDir)
#         return jsonify({'message': 'BufferFile is successfully created'}), 200
#     elif(request.method == 'PUT'):
#         fatherDir = Directory(request.args.get("father"))
#         status = 200
#         if(buffer.__move__()["error"] != ""):
#             status = 400
#         return jsonify(buffer.__move__(fatherDir)), status
#     elif(request.method == 'PATCH'):
#         status = 200
#         if(buffer.__push__()["error"] != ""):
#             status = 400
#         return jsonify(buffer.__push__(request.args.get("element"))), status
#     elif(request.method == 'DELETE'):
#         status = 200
#         if(buffer.__delete__()["error"] != ""):
#             status = 400
#         return jsonify(buffer.__delete__()), status

# @app.route('/logtext', methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def logTextApi():
#     if(request.method == 'GET'):
#         return logText.__read__()
#     if(request.method == 'POST'):
#         data = request.get_json()
#         fatherDir = Directory(data["father"])
#         logText = LogTextFile(data["fileName"], fatherDir)
#         return {'message': 'LogTextFile is successfully created'}
#     if(request.method == 'PUT'):
#         data = request.get_json()
#         fatherDir = Directory(data["father"])
#         return logText.__move__(fatherDir)
#     if(request.method == 'PATCH'):
#         data = request.get_json()
#         return logText.__log__(data["line"])
#     if(request.method == 'DELETE'):
#         return logText.__delete__()

from flask import Flask, request, jsonify
from directory import Directory
import json 
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

app = Flask(__name__)

root = Directory('root', 100)
deleted_list = []

fileName = 'binary file'
content = 'binary content'

name = 'buffer file'
size = 10

name = 'name1'
log = LogTextFile(name, root)

@app.route('/bufferfile', methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def BufferApi():
   buffer = BufferFile(name, size)
   if(request.method == 'GET'):
      return buffer.__consume__()
   elif(request.method == 'POST'):
      fatherDir = Directory(request.args.get("father"), 15)
      buffer = BufferFile(request.args.get("fileName"), request.args.get("maxSize"), fatherDir)
      return jsonify({'message': 'BufferFile is successfully created'}), 200
   elif(request.method == 'PUT'):
      fatherDir = Directory(request.args.get("father"), 15)
      return buffer.__move__(fatherDir)
   elif(request.method == 'PATCH'):
      return buffer.__push__(request.args.get("element"))
   elif(request.method == 'DELETE'):
      return buffer.__delete__()

@app.route('/binaryfile', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def BinaryApi():
   binary = BinaryFile(fileName, content, root)
   if(request.method == 'GET'):
      return jsonify(binary.__read__()), 200
   elif(request.method == 'POST'):
      fatherDir = Directory(request.args.get("father"), 15)
      binary = BinaryFile(request.args.get("fileName"), request.args.get("content"), fatherDir)
      return jsonify({'message': 'BinaryFile is successfully created'}), 200
   elif(request.method == 'PUT'):
      fatherDir = Directory(request.args.get("father"), 15)
      return jsonify(binary.__move__(fatherDir)), 200
   elif(request.method == 'DELETE'):
         return binary.__delete__()

@app.route('/directory', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def DirectoryApi():
   if request.method == 'POST':
      if any(x.name == request.args.get('name') for x in root.list) or request.args.get('name') == 'root':
         return jsonify({
         "message": "Directory already exists.",
      }), 400
      dir = Directory(request.args.get('name'), request.args.get('max_elems'), root)
      return jsonify({
         "message": "Directory created successfully.",
         "directory": {
            "parent": str(dir.parent),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)     
         }
      }), 201
      
   elif request.method == 'GET':
      if any(dir.name == request.args.get('name') for dir in root.list) or request.args.get('name') == 'root':
         if request.args.get('name') == 'root':
            dir = root
         else:
            dir = next(x for x in root.list if x.name == request.args.get('name'))
         return jsonify({
         "message": "Directory was read successfully.",
         "directory": {
            "parent": str(dir.parent),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)  
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400

   elif request.method == 'PATCH':
      if any(dir.name == request.args.get('name') for dir in root.list):
         dir = next(x for x in root.list if x.name == request.args.get('name'))
         dir.move(root)
         return jsonify({
         "message": "Directory moved successfully.",
         "directory": {
            "parent": str(dir.parent.name),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)    
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400 

   else:
      if request.args.get('name') not in deleted_list and any(dir.name == request.args.get('name') for dir in root.list):
         dir = next(x for x in root.list if x.name == request.args.get('name'))
         del dir
         deleted_list.append(request.args.get('name'))
         return jsonify({
         "message": "Directory deleted successfully.",
         }), 200
      return jsonify({
         "message": "Directory was not deleted.",
         }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')