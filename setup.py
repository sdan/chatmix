from setuptools import setup, find_packages

setup(
    name="chatmix",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    author="Surya Dantuluri",
    author_email="surya@suryad.com",
    description="A Python library for parsing conversation history from various AI chat platforms",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sdan/chatmix",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
