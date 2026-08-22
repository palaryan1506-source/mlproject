'''mostly because we are building our website as a package . So if any other person 
wants to make change, then they can do it too.'''


from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT = '-e .'  ## we included that at the end of the requirement.txt coz we want 'setup.py' to run automatically with 'requirement.txt'
def get_requirements(file_path :str)-> List[str]:
    """this function will return the list of requirements"""

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  ## this will include >> \n at the end. we need to remove it.
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(


    name = 'mlproject',
    version='0.0.1',    
    author='Aryan',
    author_email='palaryan1506@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')



)