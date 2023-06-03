from setuptools import find_packages, setup
from typing import List



with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "TextSummarizer"
AUTHOR_NAME = "Shubham Khera"
SRC_REPO = "TextSUmmarizer"
AUTHOR_EMAIL = "shubham_khera@hotmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A NLP application i.e., text summarizer project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where='src')

)


# Hyphen_e_Dot ='-e .'
# author_user_name = "shubhamkhera"
# src_repo = "TextSummarizer"

# def get_requirements(file_path:str) -> List[str]:
#     '''
#     this function will return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         [req.replace('\n', '') for req in requirements]

#         if Hyphen_e_Dot in requirements:
#             requirements.remove(Hyphen_e_Dot)



# setup(
#     name='Text Summarizer',
#     version='0.0.1',
#     author='Shubham',
#     author_email='shubham_khera@hotmail.com',
#     description="Python Packages for Text Summarizer Project",
#     url = f"https://github.com/shubhamkhera/TextSummarizer",
#     project_urls={"Bugs": f"https://github.com/shubhamkhera/TextSummarizer/issues"},
#     package_dir={"":"src"},
#     packages=find_packages(where='src'),
#     install_requires=get_requirements('requirements.txt')
# )