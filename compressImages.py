from os import listdir, mkdir
from os.path import isfile, join, isdir, exists
import sys
from PIL import Image

def compressFile(filepathWithoutFileName, fileName, quality): 
    print("arguments received") 
    print(filepathWithoutFileName)
    print(fileName)
    fullfilepath = join(filepathWithoutFileName, fileName) 
    picture = Image.open(fullfilepath) 
    dirPathCompressedImgs = join(filepathWithoutFileName, "compressed")
    
    compressedfilepath = join(dirPathCompressedImgs, fileName)
    print("compressed file will be saved at ")
    print(compressedfilepath)
    picture.save(compressedfilepath, "JPEG",  optimize = True, quality = 60 ) 
    return


def compressEachFileInGivenDir(dirPath, quality):
    print("quality param is ")
    print(quality)
    onlyfiles = [ dirEntry for dirEntry in listdir(dirPath) if isfile(join(dirPath, dirEntry)) ]
    print("files in the given dir are")
    print(onlyfiles)
    compressedDirPath = join( dirPath, "compressed" )
    if(not exists(compressedDirPath)):
        mkdir( compressedDirPath )
    for img in onlyfiles:
        compressFile(dirPath  , img, quality)

def main():
    if len(sys.argv) < 3:
        raise ValueError('please pass the directory path')

    dirPath = sys.argv[1]
    quality = int(sys.argv[2])
    compressEachFileInGivenDir(dirPath, quality)


if __name__ == "__main__": 
    main() 
