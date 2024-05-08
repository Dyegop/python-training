import os
import shutil
import re


# Variables:

path1 = (
    r'C:\Users\ponce\Documents\Education\Degree - Software Engineering\Python\Course - Python 3'
)
path2 = r'\12-Advanced Python Modules\08-Advanced-Python-Module-Exercise'
extracted_content = path1+path2+'\\extracted_content'
zip_file = path1+path2+'\\unzip_me_for_instructions.zip'
instructions_file = path1+path2+'\\extracted_content\\Instructions.txt'


pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
match = []

# Function to find patterns:
def search(file, p_pattern):
    open_file = open(file, 'r')
    text = open_file.read()
    if re.search(p_pattern, text):
        return re.search(p_pattern, text)
    else:
        return ''



# -----------SCRIPT-----------

# Unzip file:
shutil.unpack_archive(zip_file, path1+path2, "zip")

# Read the instructions file:
with open(instructions_file, 'r') as instructions:
    content = instructions.read()
    print(content)
    print("\n")

# Walk through files:
for folder, sub_folders, files in os.walk(extracted_content):
    for f in files:
        full_path = folder + '\\' + f
        match.append(search(full_path, pattern))

for r in match:
    if r != '':
        print(r.group())
