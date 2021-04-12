# bill class
class picture:
    def __init__(self,filename):
        self.__file_name = filename
    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self,filename):
        self.__file_name = filename
