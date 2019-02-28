import os
import sys
import pathlib
import inspect
import json

def isDirExists(dname):
    p = pathlib.Path(dname)
    if( p.exists()):
        if( not p.is_dir() ):
            print(f"{dname} exists but it is not a directory")
        else:
            return True, p
    return False, p

def createDir(dname:list):
    try:
        if( not isDirExists(dname)[0]):
            os.mkdir(dname)
        else:
            print(f"Directory {dname} exists")
    except:
        print("Failed to create dir {0}. Error: {1}".format(dname, sys.exc_info()))
       
def createDir(pathparts):
    try:
        path = "/".join(pathparts)
        os.makedirs(path)
        return path
    except:
        print("{0} - error : {1}".format(inspect.currentframe().f_code.co_name, sys.exc_info()))

def createFile(dname:str, fname:str):
    r, p = isDirExists(dname)
    if( r ):
        p = p.joinpath(fname)
        p.touch()
    else:
        path = createDir(list(pathlib.PurePath(dname).parts))
        r, p = isDirExists(path)
        if( r ):
            p = p.joinpath(fname)
            p.touch()
        else:
            print(f"Invalid directory {dname}")
            
def main_impl():
    try:
        rootDir = "mytestProj"
        packageMarker = "__init__.py"
        readmeFile = "README.md"
        setupFile = "setup.py"
        projDir = "test_projdir"
        mainFile = "main.py"
        dataDir = "data"
        testDir = "test"
        testMainFile = "test_main.py"

        createFile(rootDir, readmeFile)
        createFile(rootDir, setupFile)
        path = createDir([rootDir, projDir ,dataDir])
        createFile(path, packageMarker)
        createFile(path, mainFile)
        path = createDir([rootDir, projDir, testDir])
        createFile(path, packageMarker)
        createFile(path, testMainFile)
    except:
        print("Error in {0} : {1}".format(inspect.currentframe().f_code.co_name,
                                          sys.exc_info()))
        
if __name__ == "__main__":
    
    main_impl()
