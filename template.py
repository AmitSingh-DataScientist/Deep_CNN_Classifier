import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "deepCNNClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
     f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",                        # to contains all configuraions
    "dvc.yaml",                                   # to create data version control file
    "params.yaml",                                # to have all training parameters at one place
    "init_setup.sh",                              # this file will help to create an environment
    "requirements.txt",
    "requirements_dev.txt",                       # this will help in development not used in anywhere else
    "setup.py",
    "setup.cfg",                                  # this file required if we create python package only                                  
    "pyproject.toml",                             # this file required if we create python package only
    "tox.ini",                                    # this file will help in testing the project local
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)        # this will take care of file conventions based on machine
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file: {filename}")
    
    # create file only if the file is not there or file has nothing 0 kb
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"{filename} already exists")
        




