import pytest
from array import array
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile


class TestDirectory:
    fatherDirectory = Directory('fatherDir')

    def test_directoryCreation(self):
        #arrange
        maxElements = 10
        name = 'name1'
        directory = Directory(name, maxElements)

        #act
        #assert
        assert directory.name == name
        assert directory.DIR_MAX_ELEMS == maxElements
        assert directory.elementsCount == 0
        assert pytest.raises(OverflowError)

    def test_directoryMove(self):
        #arrange
        directory = Directory('dir')
        assert pytest.raises(OverflowError)

        #assert
        assert directory.__move__(self.fatherDirectory) == {'message': 'File/subdirectory moved successfully'}

    def test_directoryDeletion(self):
        #arrange
        directory = Directory('dir')

        #assert
        assert directory.__delete__() == {'message': directory.name +'directory deleted'}
        assert directory.__delete__() == {'error': 'Directory is already deleted'}

class TestBinary:
    fatherDirectory = Directory('fatherDir')

    def test_binaryCreation(self):
        #arrange
        fileName = 'name1'
        content = 'some file content blah blah blah'
        binary = BinaryFile(fileName, content, self.fatherDirectory)

        #act
        #assert
        assert binary.fileName == fileName
        assert binary.content == content
        assert binary.__read__() == {'content': content}
        assert binary.father == self.fatherDirectory

    def test_binaryMove(self):
        #arrange
        name = 'name1'
        content = 'some file content'
        binary = BinaryFile(name, content)
        assert pytest.raises(OverflowError)

        #assert
        assert binary.__move__(self.fatherDirectory) == {'message': 'File moved successfully'}

    def test_binaryRead(self):
        #arrange
        name = 'name1'
        content = 'some file content'
        binary = BinaryFile(name, content)
        assert pytest.raises(OverflowError)

        #assert
        assert binary.__read__() == {'content': 'some file content'}

    def test_binaryDeletion(self):
        #arrange
        binary = BinaryFile('bin')

        #assert
        assert binary.__delete__() == {'message': binary.fileName +'file deleted'}
        assert binary.__delete__() == {'error': 'File is already deleted'}

class TestBuffer:
    fatherDirectory = Directory('fatherDir')

    def test_bufferCreation(self):
        #arrange
        name = 'name1'
        size = 10
        buffer = BufferFile(name, size, self.fatherDirectory)

        #act
        #assert
        assert buffer.fileName == name
        assert buffer.MAX_BUF_FILE_SIZE == size
        assert pytest.raises(OverflowError)
        assert buffer.father == self.fatherDirectory

    def test_bufferMove(self):
        #arrange
        name = 'name1'
        content = 'some file content'
        buffer = BufferFile(name, content)
        assert pytest.raises(OverflowError)

        #assert
        assert buffer.__move__(self.fatherDirectory) == {'message': 'File moved successfully'}

    def test_bufferDeletion(self):
        #arrange
        buffer = BufferFile('buffer')

        #assert
        assert buffer.__delete__() == {'message': buffer.fileName +'file deleted'}
        assert buffer.__delete__() == {'error': 'File is already deleted'}

    def test_bufferAddConsume(self):
        #arrange
        name = 'name1'
        size = 10
        line1 = 'line1'
        line2 = 'line2'
        buffer = BufferFile(name, size)

        #act
        buffer.__push__(line1)
        buffer.__push__(line2)

        #assert
        assert buffer.__consume__() == {'consumed content': line1}
        assert buffer.__consume__() == {'consumed content': line2}
        assert buffer.__consume__() == {'error': 'content is empty'}
        assert pytest.raises(OverflowError)

class TestLog:
    fatherDirectory = Directory('fatherDir')

    def test_logCreation(self):
        #arrange
        name = 'name1'
        log = LogTextFile(name, self.fatherDirectory)

        #act
        #assert
        assert log.fileName == name
        assert pytest.raises(OverflowError)
        assert log.father == self.fatherDirectory

    def test_logMove(self):
        #arrange
        name = 'name1'
        log = LogTextFile(name)
        assert pytest.raises(OverflowError)

        #assert
        assert log.__move__(self.fatherDirectory) == {'message': 'File moved successfully'}

    def test_logDeletion(self):
        #arrange
        log = LogTextFile('log')

        #assert
        assert log.__delete__() == {'message': log.fileName +'file deleted'}
        assert log.__delete__() == {'error': 'File is already deleted'}

    def test_logAddRead(self):
        #arrange
        name = 'name1'
        line1 = 'line1'
        line2 = 'line2'
        log = LogTextFile(name)

        #act
        log.__log__(line1)
        log.__log__(line2)

        #assert
        assert log.__read__() == {'content':'\r\n' + line1 + '\r\n' + line2}