"""
Test the os being run and the version of python
"""


import sys

def test_OS_is_linux():
	"""
	tests if the current os is linux
	"""
	assert sys.platform == "linux"

def test_python_version():
	"""
	tests if current python version is acceptable
	"""
	assert "3.10" in sys.version or "3.11" in sys.version or "3.12" in sys.version
