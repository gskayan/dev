import pytest
import subprocfuncs as spf

def test_subproc_func():
    spf.subproc_func(5)


def test_run_subproc():
    spf.run_subproc("tree ", "./subProcPlay", runincwd="/home/gskaian/projects/py")

