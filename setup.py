import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculator",
    version="0.0.1",
    author="Prabhu K",
    author_email="prabhu.k987@gmail.com",
    description="simple calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prabhuk87/pythontdd.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
