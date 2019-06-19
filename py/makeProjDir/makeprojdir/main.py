import inspect
import sys


'''
Globals
'''
PACKAGEMARKER = "__init__.py"
READMEFILE = "README.md"
SETUPFILE = "setup.py"
DATADIR = "data"
TESTDIR = "test"

MAINCODETEMPLATE =
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
        import argparse
        pp = argparse.ArgumentParser(description="New project dir names")
        '''try:'''
        pp.add_argument("rootDir",
                        metavar="root_dir",
                        type=str,
                        help="Project root directory name")
        pp.add_argument("projDir",
                        metavar="package_dir",
                        type=str,
                        help="Project package directory name")
        pp.add_argument("--mainfile",
                        default="main.py",
                        help="main() file (default:main.py)")
        pp.add_argument("--test_mainfile",
                        default="test_main.py",
                        help="test/pytest main() file (default:test_main.py)!")
        params = pp.parse_args()
        '''except Exception as e:
            print(type(e))
            return
        '''
        print(f"Parsed arguments - {0}".format(params))
        rootDir = params.rootDir
        projDir = params.projDir
        mainFile = params.mainfile
        testMainFile = params.test_mainfile

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

        path = fu.createDir([rootDir, projDir, DATADIR])

    except Exception:
        print(f"Error in {0}:{1}".format(inspect.currentframe().f_code.co_name,
                                         sys.exc_info()))


if __name__ == "__main__":
    main_impl()
