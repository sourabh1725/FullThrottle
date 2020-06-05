import os

from setuptools import setup, find_packages


def read(fname):
	"""
	Returns content of the given file
	:param fname: file name
	:return: contents of the file
	"""
	with open(os.path.join(os.path.dirname(__file__), fname)) as file:
		return file.read()


def readlines(fname):
	"""
	Read lines from the given file and strip any non printable characters while returning
	:param fname: File name
	:return: list of lines
	"""
	with open(os.path.join(os.path.dirname(__file__), fname), 'r') as file:
		return [line.strip() for line in file]


setup(
	name='activity',
	version='1.0.0',
	author='Sourabh Kumar Pandey',
	author_email='sourabh1725pandey@gmail.com',
	url='https://github.com/sourabh1725/FullThrottle.git',
	description='FullThrottle Python code base',
	long_description=read('README.md'),
	install_requires=readlines('requirements.txt'),
	packages=find_packages()
)
