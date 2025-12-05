from setuptools import setup, find_packages

setup(
    name='CLI_project',
    version='0.0.1',
    description='A simple CLI project to create, edit, and find text in files.',
    author='Flavius Pintilie',
    author_email='flaviusepintilie@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "file_editor=CLI_project.create_file:main",
        ],
    },
    install_requires=[
        "colorama",
        'requests',
    ],
)
