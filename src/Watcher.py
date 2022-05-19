"""
Class monitoring a folder.
"""
class Watcher:
    
    def __init__(self, folder: str):
        self.__folder = folder

    
    def get_folder(self):
       return self.__folder