from os import listdir, mkdir
from os.path import isfile, join, isdir, exists
import sys
from PIL import Image
from pathlib import Path

def getThumbnailFilePathToCreate(imageFullPath):
    print("input file path is %s "% imageFullPath)
    suffix = Path(imageFullPath).suffix
    filename = Path(imageFullPath)
    filenameWithoutExtn = filename.with_suffix('')
    thumbFilenameWithoutExtn = str(filenameWithoutExtn) + "-thumb"
    print(thumbFilenameWithoutExtn)
    completeThumbFilePath = thumbFilenameWithoutExtn + suffix
    return completeThumbFilePath



def createThumbnailsForAllImages(dirPath, max_size):
    allImageFiles = recursiveDirTreeWalker(dirPath)
    for imgFilePath in allImageFiles:
        origImageHandle = Image.open(imgFilePath)
        copyOrigImageHandle = origImageHandle.copy()
        copyOrigImageHandle.thumbnail(max_size)  #this modifies image handle in place
        completeThumbnailPath = getThumbnailFilePathToCreate(imgFilePath)
        copyOrigImageHandle.save(completeThumbnailPath)
        

def recursiveDirTreeWalker(dirPath):
    dirContents = listdir(dirPath)
    files = [ join(dirPath, dirEntry) for dirEntry in dirContents if isfile(join(dirPath, dirEntry)) and isImageSuffix(join(dirPath, dirEntry)) ]
    directories = [ dirEntry for dirEntry in dirContents if  isdir(join(dirPath, dirEntry)) ]
    for a_dir in directories:
        subDir = join(dirPath, a_dir )
        files.extend(recursiveDirTreeWalker(subDir))
    return files     

def isImageSuffix(filePath):
    suffix = Path(filePath).suffix
    return suffix == ".jpg" or suffix == ".JPG" or suffix == ".jpeg" or suffix == ".JPEG" or suffix == ".png" or suffix == ".PNG"       

def main():
    if len(sys.argv) < 2:
        raise ValueError('please pass the directory path')

    dirPath = sys.argv[1]
    createThumbnailsForAllImages(dirPath, (400, 400))
    #getThumbnailFilePathToCreate("/home/chetan/personal_projects/personalWebsite/static/britainTrip/oxford/IMG_20180722_142219938.jpg")


if __name__ == "__main__": 
    main() 
