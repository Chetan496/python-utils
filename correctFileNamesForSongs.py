import sys
import re
from os import listdir, mkdir, rename
from os.path import isfile, join, isdir, exists, basename, dirname, splitext
from pathlib import Path
import string

def main():
    if len(sys.argv) < 2:
        raise ValueError('please pass the directory containing all songs')

    songDir = sys.argv[1]
    songFiles = recursiveDirTreeWalker(songDir)
    songModifications = []
    for songFile in songFiles:
        songName = basename(songFile)
        songDir = dirname(songFile)
        changeTuple = removeNumberPrefix(songName)
        if changeTuple[0] != changeTuple[1]:
            renameTuple = ( join(songDir, changeTuple[0]) , join(songDir, changeTuple[1] ) )
            songModifications.append(renameTuple)

    for modification in songModifications:
        print(modification[0], "  -->  ", modification[1])
        rename(modification[0], modification[1])



    
def removeNumberPrefix(songName):
    pattern = r'^\d+(\.|-|\s|_)*'
    modifiedName = re.sub(pattern, '', songName)
    if splitext(modifiedName)[0].isupper():
        modifiedName = string.capwords(modifiedName)
    return (songName, modifiedName)

def recursiveDirTreeWalker(dirPath):
    dirContents = listdir(dirPath)
    files = [ join(dirPath, dirEntry) for dirEntry in dirContents if isfile(join(dirPath, dirEntry)) and isSongSuffix(join(dirPath, dirEntry)) ]
    directories = [ dirEntry for dirEntry in dirContents if  isdir(join(dirPath, dirEntry)) ]
    for a_dir in directories:
        subDir = join(dirPath, a_dir )
        files.extend(recursiveDirTreeWalker(subDir))
    return files


def isSongSuffix(filePath):
    suffix = Path(filePath).suffix
    return suffix == ".mp3" or suffix == ".MP3" or suffix == ".aac" or suffix == ".wav" or suffix == ".ogg" or suffix == ".flac"


if __name__ == "__main__":
    main()