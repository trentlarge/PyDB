#!/usr/bin/env python3
from distutils.core import setup

from db import name, version

setup(
	name=name,
	version=version,
	description='A human-readable, magic database in Python',
	license='MIT',
	author='Trenton Large',
	author_email='trentonlarge@gmail.com',
	packages=['db'],
)
