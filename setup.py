from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            # ignore editable installs and comments
            if line.startswith("-e"):
                continue
            # ignore empty lines and comments
            if not line or line.startswith("#"):
                continue
            requirements.append(line.split("#")[0].strip())
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    description="Initial Learning Setup",
    author="pandeyshreyansh46@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

## On running this setup it will search in how many folders we have __init__.py file to build this
