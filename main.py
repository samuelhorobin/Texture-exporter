import os
import shutil

class MissingFileError(Exception):
    def __init__(self, directory):
        self.message = f"ERROR :: {directory} does not exist"
        super().__init__(self.message)


def getJarPath(version: str) -> str: 
    directory = os.path.join(os.getenv('APPDATA'), ".minecraft")
    if not os.path.exists(directory):
        raise MissingFileError(directory)
    
    versionPath = os.path.join(directory, "versions", version)
    if not os.path.exists(versionPath):
        raise MissingFileError(versionPath)
    
    jarPath = os.path.join(versionPath, f"{version}.jar")
    if not os.path.exists(jarPath):
        raise MissingFileError(jarPath)

def extractJarData(path):
    pass


getJarPath("1.19.2")




