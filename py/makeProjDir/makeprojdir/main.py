import os
import sys
import pathlib
import inspect

'''
Globals
'''
PACKAGEMARKER = "__init__.py"
READMEFILE = "README.md"
SETUPFILE = "setup.py"
DATADIR = "data"
TESTDIR = "test"

MAINCODETEMPLATE=\
"""
import inspect\n
\n
def main_impl():\n
\t_n_ = inspect.currentframe().f_code.co_name\n
\tprint(f\"Starting: {_n_}\")
\t\'\'\' Your code goes here \'\'\'
\tprint(f\"Stopping: {_n_}\")
\n
if __name__ ==\"__main__\":\n
\tmain_impl()\n
"""

def isDirExists(dname):
    p = pathlib.Path(dname)
    if( p.exists()):
        if( not p.is_dir() ):
            print(f"{dname} exists but it is not a directory")
        else:
            return True, p
    return False, p

      
def createDir(pathparts):
    
    path = "/".join(pathparts)
    try:
        os.makedirs(path, exist_ok=True)
    except:
        print("{0} - error : {1}".format(inspect.currentframe().f_code.co_name, sys.exc_info()))
    else:
        return path        

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
        ''' convert to commad line arguments '''
        
        rootDir = "json_playbox"
        projDir = "playwithjson"
        mainFile = "main.py"
        testMainFile = "test_main.py"

        path = createDir([rootDir])
        createFile(path, READMEFILE)
        createFile(path, SETUPFILE)
        path = createDir([rootDir, projDir])
        createFile(path, PACKAGEMARKER)
        createFile(path, mainFile)
        path = createDir([rootDir, projDir ,DATADIR])
        path = createDir([rootDir, projDir, TESTDIR])
        createFile(path, PACKAGEMARKER)
        createFile(path, testMainFile)
        with open("/".join([rootDir, projDir, mainFile]), 'w') as f:
                   f.write(MAINCODETEMPLATE)
    except:
        print("Error in {0} : {1}".format(inspect.currentframe().f_code.co_name,
                                          sys.exc_info()))
        
if __name__ == "__main__":
    main_impl()
