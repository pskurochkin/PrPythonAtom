import os.path
import pickle

class FileWriter:

    def __init__(self, path):
        self._path = path
        if self.check_path(self._path):
            self._file = None
        else:
            self._file = self._path.replace(os.path.dirname(self._path) + '/', '')

    def __enter__(self):
        self._file = open(self._path, 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        self._file = None

    def check_path(self, path):
        return os.path.isdir(path)

    def print_file(self):
        if self._file is None:
            print("Sorry, file does not exist.")
        else:
            print("file: " + self._file)
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
