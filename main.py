import os
import shutil
import pathlib

class MissingFileError(Exception):
    def __init__(self, directory):
        self.message = f"{directory} does not exist"
        super().__init__(self.message)

class ExistingFileError(Exception):
    def __init__(self, directory):
        self.message = f"{directory} already exists"
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
    
    return jarPath

def copyJarData(src, version):
    dest = os.path.join(pathlib.Path(__file__).parent, "resource packs", f"{version}.jar")
    print(src, dest)
    jarCopy = shutil.copy(src, dest)
    
def extractJarData(path):
    pass

copyJarData(getJarPath("1.19.2"), "1.19.2")




