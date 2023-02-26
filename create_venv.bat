@echo off
echo Batch script starts
if exist .\.venv\ (
    echo Disabling current existing Python virtual environment...
    call .\.venv\Scripts\deactivate.bat
    echo Deleting current existing Python virtual environment...
    rd /s .\.venv\
) else (
    echo No previous existing Python virtual environment
)
echo Creating new Python virtual environment...
python -m venv .\.venv --upgrade-deps
echo Activating the created environment
call .\.venv\Scripts\activate.bat
echo Installing Python modules to the virtual environment...
pip install --upgrade pip
pip install pandas
pip install openpyxl

echo Deactivating the created environment
call .\.venv\Scripts\deactivate.bat
echo For activating it again, please run "call.bat". All done!


 