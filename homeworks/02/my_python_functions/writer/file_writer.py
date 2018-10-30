import os.path
import pickle

class FileWriter:

    def __init__(self, path):
        if self.check_path(self._path):
            self._path = path
            self._file = None

    def __enter__(self):
        self._file = open(self._path, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        self._file = None

    def check_path(self, path):
        return os.path.exists(path) and os.path.isfile(path)

    path = property()

    @path.getter
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        if self.check_path(new_path):
            self.__init__(new_path)

    @path.deleter
    def path(self):
        self._path = ''

    def print_file(self):
        if self._file is None:
            print("Sorry, file does not exist.")
        else:
            self._file = open(self._path, 'r')
            print(self._file.read())
            self._file.close()

    def write(self, some_string):
        self._file.write(some_string)

    def save_yourself(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, "rb") as file:
            return pickle.load(file)
