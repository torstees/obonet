import os
import re
import subprocess

import setuptools


directory = os.path.dirname(os.path.abspath(__file__))

# version
init_path = os.path.join(directory, 'obo', '__init__.py')
with open(init_path) as read_file:
    text = read_file.read()
pattern = re.compile(r"^__version__ = ['\"]([^'\"]*)['\"]", re.MULTILINE)
version = pattern.search(text).group(1)

# long_description
readme_path = os.path.join(directory, 'README.md')
try:
    # Try to create an reStructuredText long_description from README.md
    args = 'pandoc', '--from', 'markdown', '--to', 'rst', readme_path
    long_description = subprocess.check_output(args)
    long_description = long_description.decode()
except Exception as error:
    # Fallback to markdown (unformatted on PyPI) long_description
    print('README.md conversion to reStructuredText failed. Error:')
    print(error)
    with open(readme_path) as read_file:
        long_description = read_file.read()


setuptools.setup(
    name = 'obo',
    version = version,
    author = 'Daniel Himmelstein',
    author_email = 'daniel.himmelstein@gmail.com',
    url = 'https://github.com/dhimmel/obo',
    description = 'OBO ontology tools in python',
    long_description = long_description,
    license = 'CC0',
    packages = ['obo'],
    install_requires = ['networkx'],
    )
