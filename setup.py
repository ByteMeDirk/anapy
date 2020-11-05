import setuptools

with open("README.rst", "r") as file_stream:
    readme = file_stream.read()

with open("requirements.txt", "r") as file_stream:
    install_requires = file_stream.read().splitlines()

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
]

project_urls = {}

setuptools.setup(
    author="DirksCGM",
    classifiers=classifiers,
    description="ANApy is a universal data manipulation tool "
                "for handling all major forms of data on the fly",
    install_requires=install_requires,
    license="GNU",
    long_description=readme,
    long_description_content_type="text/x-rst",
    name="anapy",
    python_requires=">=3.6.1",
    url="https://github.com/DirksCGM/anapy",
    version='0.1.0'
)
