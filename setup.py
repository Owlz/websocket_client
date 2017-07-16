# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
long_description = "See website for more info."

setup(
    name='websocket_client',

    version='0.0.1',

    description='Simple synchronous websocket client.',
    long_description=long_description,

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['websockets'],

    entry_points={
        'console_scripts': [
            'websocket_client = websocket_client.websocket_client:shell',
        ],
    },
)

