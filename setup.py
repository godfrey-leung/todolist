import setuptools

with open('requirements.txt', 'r') as fh:
    install_requirements = fh.readlines()

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_todolist",
    version="1.0.0"
    author="Godfrey Leung",
    author_email="godfrey.leung.cosmo@gmail.com",
    description="Creating a simple to do list",
    long_description=long_description,
    long_description_content_type='text/markdown',
#    url='https://github.com/Team-Cloudbusters/cloudbusting',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=install_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
