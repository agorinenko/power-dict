import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="power_dict",
    version="0.0.9",
    author="Gorinenko Anton",
    author_email="anton.gorinenko@gmail.com",
    description="Library for easy work with the python dictionary",
    long_description=long_description,
    keywords='python, dict, utils',
    long_description_content_type="text/markdown",
    url="https://github.com/agorinenko/power-dict",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'try-parse'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.7',
)
