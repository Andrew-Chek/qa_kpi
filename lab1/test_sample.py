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

        #act
        directory.__move__(self.fatherDirectory)

        #assert
        assert directory.father == self.fatherDirectory

    def test_directoryDeletion(self):
        #arrange
        directory = Directory('dir')

        #act
        del directory

        #assert
        assert 'directory' not in locals()

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
        assert binary.__read__() == content
        assert binary.father == self.fatherDirectory

    def test_binaryMove(self):
        #arrange
        name = 'name1'
        content = 'some file content blah blah blah'
        binary = BinaryFile(name, content)
        assert pytest.raises(OverflowError)

        #act
        binary.__move__(self.fatherDirectory)

        #assert
        assert binary.father == self.fatherDirectory

    def test_binaryDeletion(self):
        #arrange
        binary = BinaryFile('bin')

        #act
        del binary

        #assert
        assert 'binary' not in locals()

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

        #act
        buffer.__move__(self.fatherDirectory)

        #assert
        assert buffer.father == self.fatherDirectory

    def test_bufferDeletion(self):
        #arrange
        buffer = BufferFile('buffer')

        #act
        del buffer

        #assert
        assert 'buffer' not in locals()

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
        assert buffer.__consume__() == line1
        assert buffer.__consume__() == line2
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

        #act
        log.__move__(self.fatherDirectory)

        #assert
        assert log.father == self.fatherDirectory

    def test_logDeletion(self):
        #arrange
        log = LogTextFile('log')

        #act
        del log

        #assert
        assert 'log' not in locals()

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
        assert log.__read__() == '\r\n' + line1 + '\r\n' + line2