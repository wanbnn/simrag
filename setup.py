from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simrag",
    version="0.1.0",
    author="wanbnn",
    author_email="wanbnn@outlook.com.br",
    description="A simple RAG lib to easy use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wanbnn/simrag",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)