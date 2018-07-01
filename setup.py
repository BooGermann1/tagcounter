import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tagcounter",
    version="0.0.1",
    author="Sergei Rybin",
    author_email="sergei_rybin@epam.com",
    description="A program for python course training",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "TOPIC :: EDUCATION",
    ),
    include_package_data=True,

    package_data={
        'data':['data/log.txt',
                'data/prompt.txt',
                'data/tagcounter.db']
    },

    entry_points={
       'console_scripts': [
           'tagcounter = tagcounter:main',
       ],
    },
)

