import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(meassage)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", #Later Delete this
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "dockerFile.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info("Creating directory:{fileDir} for the file {fileName}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath, 'w') as f:
            pass
            logging.info(f"Creating Empty file: {filePath} ")
    else:
        logging.info(f"{fileName} already exist")