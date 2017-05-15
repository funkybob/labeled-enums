
from setuptools import setup

with open('README.md') as fin:
    description = fin.read()

setup(
    name='labeled-enum',
    version='1.0.2',
    description='Django friendly, iterable Enum type with labels.',
    long_description=description,
    author='Curtis Maloney',
    author_email='curtis@tinbrain.net',
    py_modules=['lenum',],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
    ],
)
