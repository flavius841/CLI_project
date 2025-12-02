from setuptools import setup, find_packages

setup(
    name='CLI_project',
    version='0.0.1',
    description='Example package for a CLI',
    author='Flavius Pintilie',
    author_email='flaviusepintilie@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create-file=CLI_project.create_file:create',
            'upload=CLI_project.create_file:upload',
        ],
    },
    install_requires=[
        'requests',
    ],
)
