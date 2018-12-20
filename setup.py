import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="catpictures",
    version="1",
    author="Giacomo Lawrance",
    author_email="thenerdystudent@gmail.com",
    description="Open a picture of a cat in a new tab on your browser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giacomolaw/catpictures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)