import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="anapy",
    version="0.0.1",
    author="DirksCGM",
    author_email="dirkscgm@gmail.com",
    description="an analytical toolset for working on datasets of various formats",
    license="MIT",
    keywords="python, analytics",
    url="https://github.com/DirksCGM/anapy",
    install_requires=[
        'pandas~=1.1.3',
        'setuptools~=50.3.0',
        'Cython~=0.29.21',
        'pyyaml~=5.3.1'
    ],
    long_description=read('README.md'),
    python_requires=">=3.6.1"
)
