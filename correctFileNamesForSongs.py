import sys
import re
from os import listdir, mkdir
from os.path import isfile, join, isdir, exists

def main():
    if len(sys.argv) < 2:
        raise ValueError('please pass the directory containing all songs')

    songDir = sys.argv[1]
    songFiles = [ dirEntry for dirEntry in listdir(songDir) if isfile(join(songDir, dirEntry)) ]
    for song in songFiles:
        removeNumberPrefix(song)
    
    
def removeNumberPrefix(songName):
    pattern = r'^\d+'
    modifiedName = re.sub(pattern, '', songName)
    print("rename %s -> %s "% (songName ,modifiedName))



def recursiveDirTreeWalker(dirPath):
    files = [ dirEntry for dirEntry in listdir(dirPath) if isfile(join(dirPath, dirEntry)) ]


if __name__ == "__main__":
    main()