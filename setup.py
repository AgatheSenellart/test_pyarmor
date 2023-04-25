from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="multivae",
    version="0.0.1",
    author="Agathe Senellart (HekA team INRIA)",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AgatheSenellart/test_pyarmor",

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy",
        
    ],
    extras_require={':python_version == "3.7.*"': ["pickle5"]},
    python_requires=">=3.7",
)
