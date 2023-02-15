@echo off
echo Batch script starts
if exist .\.venv\ (
    echo Disabling current existing Python 3 virtual environment...
    call .\.venv\Scripts\deactivate.bat
    echo Deleting current existing Python 3 virtual environment...
    rd /s .\.venv\
) else (
    echo No previous existing Python 3 virtual environment
)
echo Creating new Python 3 virtual environment...
python3 -m venv .\.venv
echo Activating the created environment
call .\.venv\Scripts\activate.bat
echo Installing Python modules to the virtual environment...
pip install --upgrade pip

echo Deactivating the created environment
call .\.venv\Scripts\deactivate.bat
echo For activating it again, please run "call.bat". All done!


 