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
                
def main_impl():

    import fileutils as fu

    try:
        ''' convert to commad line arguments '''
        
        rootDir = "json_playbox"
        projDir = "playwithjson"
        mainFile = "main.py"
        testMainFile = "test_main.py"

        path = rootDir
        fu.createFile(path, READMEFILE)
        fu.createFile(path, SETUPFILE)
        
        path = fu.createDir([rootDir, projDir])
        fu.createFile(path, PACKAGEMARKER)
        fu.createFile(path, mainFile)

        def writeTemplateMain(filepath):
            with open(filepath, 'w') as f:
                f.write(MAINCODETEMPLATE)

        writeTemplateMain("/".join([path, mainFile]))
        
        path = fu.createDir([rootDir, projDir, TESTDIR])
        fu.createFile(path, PACKAGEMARKER)
        fu.createFile(path, testMainFile)
        
        path = fu.createDir([rootDir, projDir ,DATADIR])
        
    except:
        print("Error in {0} : {1}".format(inspect.currentframe().f_code.co_name,
                                          sys.exc_info()))
        
if __name__ == "__main__":
    main_impl()
