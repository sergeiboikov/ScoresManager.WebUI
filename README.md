# ScoresManager.WebUI

## Installation
1. Clone code from this repo
2. Install python from https://www.python.org/downloads/
3. Create a new virtual environment in the folder with cloned project: `python -m venv venv`
4. Activate the created virtual environment: `venv\Scripts\activate`
5. Install all the necessary libraries from requirements: `pip install -r requirements.txt`

## Configuration
1. Edit the `smgr_config.yaml` file:
   - Change the value for `workingpath` to your root folder with project
   - Change the values for `host`, `username` to actual
2. Create Environment variable with name `ENVOS_SMGR_VALUE_01` and value: password for ScoresManagerDB database

## Execution
1. Run the file `main.py`
2. Open in browser `http://127.0.0.1:5000/`