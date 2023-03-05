import sys
import pandas as pd
from tkinter import filedialog

def get_target_var_row_index(line, sw_name_list):
    """
    # Get target variable row index

    Look for one of the variable software names in a text file line.
    If an affectation to one of them is found, then return the Excel 
    row (or pandas Dataframe row) to which the variable corresponds.
    An affectation should look like:
        - "<variable_name>=" or
        - "<variable_name> ="
    
    Parameters:
        line (str):     [Input] Line of the text file to be parsed
        sw_name_list:   [Input] Variables software name list (in dataframe or Excel order)
    Return:
        index (int):    Index to which the affectation variable is associated to.
                        If no variable affectation is found, returns -1.
        str_pos (int):  Position in the string where the affectation string ends.
                        If no variable affectation is found, returns -1.
    """
    # TODO: Cath error in input types
    line = str(line)
    
    # Initialize return
    index = -1
    str_pos = -1

    # Loop in software variable names
    for i in range(len(sw_name_list)):
        varname = sw_name_list[i][0]
        affect_str1 = varname + "="
        affect_str2 = varname + " ="
        if (affect_str1 in line):
            index = i
            str_pos = line.index(affect_str1) + len(affect_str1)
        elif (affect_str2 in line):
            index = i
            str_pos = line.index(affect_str2) + len(affect_str2)

    return index, str_pos

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
var_names = [name for name in col_names if "param" in name.lower()]
equation_col_names = [name for name in col_names if "equation" in name.lower()]
print(col_names)
print(sw_col_names)

# Get software variable names
sw_names = df[sw_col_names].values
print(sw_names)

# Get parameter names
orig_names = df[var_names].values
print(orig_names)

# Get equations
equations = df[equation_col_names].values
print(equations)

# Read source file content
with open(sourcePath, 'r') as file:
    lines = file.readlines()

newlines = list()
isWriteEnabled = False
for line in lines:
    # Copy original line to new line
    newline = line

    # As code automation starting mark is found
    if WRITING_START_MARK in line:
        isWriteEnabled = True
    
    # When code automation is running and a software var name is found in the line
    if isWriteEnabled:
        varidx, pos = get_target_var_row_index(line, sw_names)
        if varidx != -1:
            newline = "{} {}; // {}\n".format(line[0:pos],str(varidx),orig_names[varidx][0])
    
    # Add new line to the str list
    newlines.append(newline)
    
# Write content to source file
with open(sourcePath, 'w') as file:
    file.writelines(newlines)

