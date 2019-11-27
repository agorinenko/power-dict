import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="powerdict",
    version="0.0.1",
    author="Gorinenko Anton",
    author_email="anton.gorinenko@gmail.com",
    description="Library for easy work with the python dictionary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agorinenko/power_dict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
