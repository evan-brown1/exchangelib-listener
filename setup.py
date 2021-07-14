from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='exchangelib_listener',
    version='1.0.0',
    author='Evan Brown',
    description='Simple inbox event listener',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/evan_brown/exchangelib-listener',
    packages=find_packages(exclude=('test.*')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)