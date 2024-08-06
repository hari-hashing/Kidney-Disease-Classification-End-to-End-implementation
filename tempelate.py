import os
from pathlib import Path
import logging

#  logging string

# to log every task execution 
logging.basicConfig(level=logging.INFO, filename='task_execution.log', format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'Disease_classification'

list_of_files = [
    ".github/workflows/.gitkeep",
    # at time of ci/cd the above file will be removed 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]

#  as we ahve given the forward slasg in windows but only mac and linux only 
#  we have given the path to teh Path class 
#  for linux and mac it will be very fine and we do not need to pass in the Path class
#  it will detect the os and convert the pathto the windows os path 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file : {filename}")
 
    if((not os.path.exists(filepath)) or (os.path.getsize(filepath)) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"The file {filename} aleady exixts")
