import setuptools
from pgnlp import __version__

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="pgnlp",
  version=__version__,
  description="Python package for NLP",
  url="https://github.com/porfyriosg/pgnlp",
  packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['nlpcli=pgnlp.cli:main'],
    },
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: Unix Based",
  ],
)