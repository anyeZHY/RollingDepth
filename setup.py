from setuptools import setup, find_packages

def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="rollingdepth",
    version="1.0",
    packages=find_packages(),  # Automatically find all packages (my_folder, inference, etc.)
    install_requires=read_requirements('requirements.txt'),
)
