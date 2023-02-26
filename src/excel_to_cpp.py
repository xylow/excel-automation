import sys
import pandas as pd
from tkinter import filedialog

WRITING_START_MARK = "-###-"

# Get Excel file path
excelPath = filedialog.askopenfilename(initialdir=".", title="Select the Excel file to be read")
if excelPath == "":
    print("No file selected. EOP.")
    sys.exit()

# Open Excel file to pandas dataframe
print("Loading Excel file...")
df = pd.read_excel(excelPath)

# Get source file
sourcePath = filedialog.askopenfilename(initialdir=".", title="Select the souce file to be edited")
if sourcePath == "":
    print("No file selected. EOP.")
    sys.exit()

# Get Excel column names
col_names = df.columns.values.tolist()
sw_col_names = [name for name in col_names if "sw" in name.lower()]
equation_col_names = [name for name in col_names if "equation" in name.lower()]
print(col_names)
print(sw_col_names)

# Get software variable names
sw_names = df[sw_col_names]
print(sw_names)

# Get equations
equations = df[equation_col_names]
print(equations)

# Read source file content
with open(sourcePath, 'r') as file:
    lines = file.readlines()

# TODO: Edit file content
isWriteEnabled = False
for line in lines:
    if WRITING_START_MARK in line:
        isWriteEnabled = True
        continue
    if isWriteEnabled:
        # TODO: Continue here
        pass

# Write content to source file
with open(sourcePath, 'w') as file:
    file.writelines(lines)

with open(sourcePath, 'r') as file:
    for line in file:
        if isWriteEnabled:
            file.write
        if WRITING_START_MARK in line:
            isWriteEnabled = True
