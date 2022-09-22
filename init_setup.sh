echo [$(date)]: "START"
echo [$(date)]: "creating env with python 3.8 version"
# conda create --prefix venv python=3.8 -y
conda create --prefix ./env python=3.8 -y # update version
echo [$(date)]: "activating the environment"
source activate ./env
# source activate venvclear
echo [$(date)]: "installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"