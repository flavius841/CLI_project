import setuptools
from distutils.core import setup


setup(
    name='CLI_project',
    version='0.0.0',
    description='Example package for a CLI',
    author='Flavius Pintilie',
    author_email='flaviusepintilie@gmail.com',
    packages=['CLI_project'],
    entry_points={
        'console_scripts': ['cli-example=CLI_project.entry:cli_entry_point'],
    },
    install_requires=[
        'requests',
    ],
)

