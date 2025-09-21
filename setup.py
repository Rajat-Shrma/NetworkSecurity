'''
A setup.py file is the build script for a Python project. 
It tells Python (and packaging tools like pip) how to install your package, what dependencies it needs, and other metadata about your project.
'''

from setuptools import setup,find_packages
from typing import List
HYPHEN_E_DOT='-e .'

def get_requirements(file_path)->List[str]:
    try:
        with open(file_path,'r') as file:
            requirements=[line.strip() for line in file.readlines()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
        return requirements
        

    except Exception as e:
        # raise CustomException(e,sys)
        pass


setup(
    name="Network Security",
    version='0.0.0.1',
    author='Rajat',
    author_email='rajattsharma87077@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)