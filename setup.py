from setuptools import setup, find_packages

from lampy import __minimum_python_version__

setup(
    name='lampy',
    version=__minimum_python_version__,
    description='A practice Python package.',

    url='https://github.com/seanthelam/lampy',
    author='Sean Lam',
    author_email='s_lam2023@coloradocollege.edu',

    packages=find_packages(exclude=['tests', 'tests.*']),
)
