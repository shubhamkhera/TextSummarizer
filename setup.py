from setuptools import find_packages, setup
from typing import List

Hyphen_e_Dot ='-e .'
author_user_name = "shubhamkhera"
src_repo = "TextSummarizer"

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n', '') for req in requirements]

        if Hyphen_e_Dot in requirements:
            requirements.remove(Hyphen_e_Dot)



setup(
    name='Text Summarizer',
    version='0.0.1',
    author='Shubham',
    author_email='shubham_khera@hotmail.com',
    description="Python Packages for Text Summarizer Project",
    url = f"https://github.com/shubhamkhera/TextSummarizer",
    project_urls={"Bugs": f"https://github.com/shubhamkhera/TextSummarizer/issues"},
    package_dir={"":"src"},
    packages=find_packages(where='src'),
    install_requires=get_requirements('requirements.txt')
)