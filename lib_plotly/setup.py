# setup.py
from setuptools import setup, find_packages

setup(
    name='lib_plotly',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'plotly>=5.0.0',  # Add any other dependencies you might need
    ],
    description='A package for custom Plotly themes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='l0tte',
    url='https://github.com/lottedieleman/plotly-lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)


