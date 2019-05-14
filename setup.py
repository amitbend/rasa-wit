import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rasa_wit",
    version="0.1.2",
    author="Amit Bendor",
    author_email="rhcpamit@gmail.com",
    description="rasa_core interpreter connecting to Wit.ai API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amitbend/rasa-wit",
    packages=["rasa_wit"],
    install_requires=["wit~=5.1", "rasa-core~=0.14"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)