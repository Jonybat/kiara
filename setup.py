from distutils.core import setup
import os, os.path

data_files = [(os.path.expanduser('~/.kiara'), ['kiararc'])]

setup(
	name='kiara',
	version='1.1.1',
	description='Kiara updates your anidb list and sorts your anime',
	author='Bjørn Hartfelt',
	author_email='b.hartfelt@gmail.com',
	url='https://github.com/hartfelt/kiara',
	packages=['libkiara'],
	scripts=['kiara'],
	data_files=data_files,
)
