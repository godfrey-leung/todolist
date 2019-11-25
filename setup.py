import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), 'r') as fh:
    install_requirements = fh.readlines()

with open(path.join(here, 'README.md'), 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_todolist",
    version="1.0.0",
    author="Godfrey Leung",
    author_email="godfrey.leung.cosmo@gmail.com",
    description="Creating a simple to do list",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/godfrey-leung/todolist',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=install_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
