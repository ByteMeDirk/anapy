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
    url="",
    packages=['pandas', 'tests'],
    long_description=read('README.md'),
    python_requires=">=3.6.1"
)
