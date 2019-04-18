import pytest
import makeprojdir.fileutils as fu


def test_isDirExists():
    r, p = fu.isDirExists("./newdir")
    assert(r == False )
    r, p = fu.isDirExists("../test")
    assert(r == True)

def test_createDir_deleteDirs(tmpdir):
    import datetime as dt
    test_dir_name_prefix = "test_dir-"
    test_dir_name = test_dir_name_prefix + str(dt.datetime.now())
    path = fu.createDir([".", test_dir_name])
    ''' make sure dups are ignored '''
    path = fu.createDir([".", test_dir_name])
    path = fu.createDir([".", test_dir_name])

    r, p = fu.isDirExists(test_dir_name)
    assert(r == True)
    ''' Now clean up '''
    fu.deleteDirs(test_dir_name_prefix + "*")
    fu.deleteDirs(test_dir_name_prefix + "*")
    fu.deleteDirs(test_dir_name_prefix + "*")
    r, p = fu.isDirExists(test_dir_name)
    assert(r == False)

def test_deleteDirs_Exception():
    with pytest.raises(OSError):
        fu.deleteDirs("./non_existent_dir")
    

    
