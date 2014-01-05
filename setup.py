import re

from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

version = None
for line in open('./deezer/__init__.py'):
    m = re.search('__version__\s*=\s*(.*)', line)
    if m:
        version = m.group(1).strip()[1:-1]  # quotes
        break
assert version

setup(
    name='deezer',
    version=version,
    description='A friendly wrapper library for the Deezer API',
    author='Bruno Alla',
    author_email='alla.brunoo@gmail.com',
    url='https://github.com/brwoniebroke/deezer-python',
    license='BSD',
    packages=['deezer'],
    include_package_data=True,
    use_2to3=True,
    package_data={
        '': ['README.rst']
    },
    install_requires=[
    ],
    tests_require=[
        'nose>=1.1.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
