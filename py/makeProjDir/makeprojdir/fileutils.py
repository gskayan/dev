import os
import sys
import pathlib

def isDirExists(dname:str):
    p = pathlib.Path(dname)
    if( p.exists()):
        if( not p.is_dir() ):
            print(f"{dname} exists but it is not a directory")
        else:
            return True, p
    return False, p

      
def createDir(pathparts:list):
    
    path = "/".join(pathparts)
    try:
        os.makedirs(path, exist_ok=True)
    except:
        print("{0} - error : {1}".format(inspect.currentframe().f_code.co_name, 
                                         sys.exc_info()))
    else:
        return path   

def deleteDirs(path_pattern:str):
    import glob
    try:
        for d in glob.iglob(path_pattern):
            os.rmdir(d)
    except OSError as e:
        print(f"Error deleting directory: {0}".format(str(e)))
        raise e
        
    

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
