# ScoresManager.WebUI
Flask web application for ScoresManagerDB

## Installation
1. Clone code from this repo
2. Install python from https://www.python.org/downloads/
3. Open a terminal. For example, Powershell, CMD, or Bash
4. Open the `src` folder in the opened terminal: `cd "{project_folder}\src"`. For example, `cd "D:\GIT\MSBI.LAB\_RNT\ScoresManager.WebUI\src"`
5. Execute the command for creating a new virtual environment: `python -m venv venv`
6. Activate the created virtual environment: `venv\Scripts\activate`
7. Install all the necessary libraries from requirements: `pip install -r requirements.txt`

## Configuration
1. In Windows open "System Properties -> Environment Variables..."
2. Create the following "System variables":
   - `ENVOS_SMGR_VALUE_02` - Host name (`...4a.mdb.yandexcloud.net`)
   - `ENVOS_SMGR_VALUE_04` - Port (For example, `6432`)
   - `ENVOS_SMGR_VALUE_03` - Database name (For example, `ScoresManagerDB`)
   - `ENVOS_SMGR_VALUE_06` - Username (For example, `mentor`)
   - `ENVOS_SMGR_VALUE_01` - User password

## Execution
1. Run application: `python app.py`
2. Open in browser `http://127.0.0.1:5000/`
3. For login enter your email and password