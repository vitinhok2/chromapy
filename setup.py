from setuptools import setup, find_packages

setup(
    name="chromapy",
    version="0.1.0",
    author="Victor",
    author_email="victorhugooliveiragolveia@gmail.com",
    description="🖌️ A Python library for advanced color manipulation and styling in terminal applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vitinhok2/chromapy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',



)