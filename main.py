import os
import shutil
import pathlib
import zipfile
import filecmp
from PIL import Image

class MissingFileError(Exception):
    def __init__(self, directory):
        self.message = f"{directory} does not exist"
        super().__init__(self.message)

class ExistingFileError(Exception):
    def __init__(self, directory):
        self.message = f"{directory} already exists"
        super().__init__(self.message)

def get_jar_path(version: str) -> str: 
    directory = os.path.join(os.getenv('APPDATA'), ".minecraft")
    if not os.path.exists(directory):
        raise MissingFileError(directory)
    
    versionPath = os.path.join(directory, "versions", str(version))
    if not os.path.exists(versionPath):
        raise MissingFileError(versionPath)
    
    jarPath = os.path.join(versionPath, f"{version}.jar")
    if not os.path.exists(jarPath):
        raise MissingFileError(jarPath)
    
    return jarPath

def copy_jar_data(src: str, dest: str): shutil.copy(src, dest)

def extract_textures(srcJar, folderPath, outputDir):
    try:
        with zipfile.ZipFile(srcJar) as jarFile:
            for filePath in jarFile.namelist():
                if filePath.startswith(folderPath):
                    subPath = os.path.relpath(filePath, folderPath)
                    subPath = subPath.replace('/', os.path.sep)  # replace forward slashes with backslashes
                    output_path = os.path.join(outputDir, subPath)
                    if os.path.isdir(filePath):
                        os.makedirs(output_path, exist_ok=True)
                    else:
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        with open(output_path, 'wb') as outputFile:
                            outputFile.write(jarFile.read(filePath))
    except zipfile.BadZipFile as error:
        print(error)

def get_default_textures(version):
    jarDest = os.path.join(pathlib.Path(__file__).parent, "resource packs", f"{version}.jar")
    textureDest = os.path.join(pathlib.Path(__file__).parent, "resource packs", f"{version}")

    if not os.path.exists(textureDest):
        jarSrc = get_jar_path(version)
        print(f"Copying jar data from {jarSrc}...")
        copy_jar_data(jarSrc, jarDest)
        print(f"Jar data copied to {jarDest}")

        print(f"Extracting texure folder from {jarDest}...")
        extract_textures(jarDest, "assets", textureDest)
        os.remove(jarDest)
        print(f"Extracted texture to {textureDest}")

        return textureDest
    return textureDest

if __name__ == "__main__":
    version = input("Enter texture pack version\n")
    defaultTexturePath = get_default_textures(version)

    



