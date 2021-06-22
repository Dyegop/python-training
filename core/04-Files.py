import os
import shutil
import send2trash as s2t
import zipfile as zf
from PIL import Image
from pathlib import Path



# -----------------FILE MANAGEMENT-----------------

# Create files using open function
# open(filename, 'file_mode') -> open a file in a given file mode
# add r before file path avoids special characters (like \n). Alternatively, we can use \\
filename = r'C:\Users\ponce\Documents\Education\Degree - Software Engineering\Python\Course - Python 3\12-Advanced ' \
           r'Python Modules\practice.txt '
f = open(filename, 'w+')

# Create files using with statement
# Using "with", the file will automatically be closed
with open(filename, 'w+') as my_file:
    my_file.close()

# File modes
# 'w'  -> writing mode
# 'w+' -> writing and reading mode, overwrites the existing file
# 'wb' -> write and binary permissions
# 'r'  -> reading mode
# 'r+' -> reading and writing mode
# 'a'  -> appending mode

# File operations
# read()          -> return the content of a file
# readlines()     -> return a list of string values from the file, one string for each line of text
# write('string') -> write some string on a file
# close()         -> close a file
print(f.read())
print(f.readlines())
f.write('test')
f.close()

# Remove files and directories
# os.unlink/remove(path) -> delete a file at the path your provide. It can't be reversed
# os.rmdir(path)         -> delete an empty directory at the path your provide. It can't be reversed
# shutil.rmtree(path)    -> delete all files and folders contained in the path. It can't be reversed
# send2trash(path)       -> send files to trash can instead of remove them
s2t.send2trash(filename)

# Grant permissions
# os.chmod(path, mode) -> change permissions of path using mode
# mode can be an octal (for example, Oo644) or a stat variable from stat module
os.chmod(filename, 0o644)






# -----------------PATHS AND DIRECTORIES-----------------

# os.getcwd() -> return current working directory
# os.chdir()  -> change current working directory
print(os.getcwd())
os.chdir('C:\\Windows\\System32')

# os.makedirs() -> create a folder in the given directory
os.makedirs('C:\\Users\\ponce\\Documents\\test')

# os.listdir() -> list files in the current or a given directory as a list of strings
print(os.listdir())
print(os.listdir(r"C:\Users"))

# Check files or directories
# os.path.isabs(path)  -> return True if the argument is an absolute path
# os.path.isfile(path) -> return True if the argument is an existing regular file
# os.path.isdir(path)  -> return True if the argument is an existing directory
print(os.path.isabs(os.getcwd()))
print(os.path.isfile(filename))
print(os.path.isdir(filename))

# Get paths as strings
# os.path.abspath(path)        -> return a string of the absolute path of the argument
# os.path.relpath(path, start) -> return a string of a relative path from the start
# os.path.basename(path)       -> return a string of everything that comes after the last slash in a path
# os.path.dirname(path)        -> return a string of everything that comes before the last slash in a path
# os.path.split()              -> return a tuple that contains path’s dir name and base name as strings
os.path.abspath('.\\Games')  # .  -> shorthand for the current directory
os.path.isabs('..\\Games')   # .. -> shorthand for the parent folder
os.path.relpath('C:\\Windows', 'C:\\')

# Get status of a file or directory
# os.stat(path) -> performs stat() system call on the specified path, so we get status of the specified path
# The returned ‘stat-result’ object has following attributes:
# st_mode  -> It represents file type and file mode bits (permissions)
# st_dev   -> It represents the identifier of the device on which this file resides
# st_uid   -> It represents the user identifier of the file owner
# st_gid   -> It represents the group identifier of the file owner
# st_size  -> It represents the size of the file in bytes
# st_atime -> It represents the time of most recent access in seconds
# st_mtime -> It represents the time of most recent content modification in seconds
# st_ctime -> It represents the time of most recent metadata change on Unix and creation time on Windows in seconds
status = os.stat(os.getcwd())

# Move and copy directories with shutil library
# shutil.move(filename, path)   -> move or rename files
# shutil.copy(filename, path)   -> copy files or folders
# shutil.copytree(folder, path) -> copy an entire folder (including files and subfolders)
shutil.move(filename, r'C:\Users\ponce')
shutil.copy(filename, r'C:\Users\ponce')
shutil.copy(filename, r'C:\Users\ponce\new_name.txt')  # copy file and gives the copy a different name
shutil.copytree(r'C:\Users\ponce\Documents\Personal', r'C:\Users\ponce')

# Walk through a directory
# os.walk(path) -> generate the file names in a directory tree by walking the tree either top-down or bottom-up
for root, sub_folders, files in os.walk(r'C:\Users\ponce\Downloads'):
    print("Currently looking at folder: " + root)
    print('Subfolders: ')
    for sub_fold in sub_folders:
        print('\t Subfolder: ' + sub_fold)
    print('Files are: ')
    for f in files:
        print('\t File: ' + f)
    print('\n')






# ------------------PATH LIBRARY (ONLY PYTHON 3.5+)-----------------

# Path.cwd()   -> return current working directory
# Path.home()  -> return home directory
# Path().mkdir ->  create a folder in the given directory
print(Path.cwd())
print(Path.home())
Path('C:\\Users\\ponce\\Documents\\test').mkdir()

# Getting the Parts of a File Path
# anchor  -> root folder of the filesystem
# drive   -> single letter that often denotes a physical storage
# name    -> a string representing the final path component, excluding the drive and root
# stem    -> final path component, without its suffix
# suffix  -> file extension of the final component
# parent  -> folder that contains the file
# parents -> evaluates to the ancestor folders of a Path object with an integer index
# The name of the file, made up of the stem (or base name) and the suffix (or extension)
p = Path('C:\\Users\\ponce\\Documents\\example.txt')
print(p.anchor, p.name, p.stem, p.suffix, p.drive)
print(Path.cwd().parents[0])
print(Path.cwd().parents[2])

# glob() -> list the contents of a folder according to a pattern
# glob returns a generator object, that can be turned into a list
p = Path('C:\\Users\\ponce\\Desktop')
print(list(p.glob('*')))  # the asterisk stands for "multiple of any characters"
print(list(p.glob('*.txt')))  # lists all text files

# exists()  -> return True if the path exists
# is_file() -> return True if the path exists and is a file
# is_dir()  -> return True if the path exists and is a directory
winDir = Path('C:\\Windows')
calcFile = Path('C:\\Windows\\System32\\calc.exe')
winDir.exists()
calcFile.is_file()
calcFile.is_dir()






# ------------------ZIPPING FILES-----------------

# zipfile() -> zip files to compress them
# To compress a file, create a zip file object, then write to it (the write step compresses the files)
# To compress all files in a folder, just use the os.walk() method to iterate this process
compressed_file = zf.ZipFile('comp_file.zip', 'w')
compressed_file.write("new_file.txt", compress_type=zf.ZIP_DEFLATED)
compressed_file.close()

# extractall() -> extract files in a folder
# extract()    -> extract individual file
zip_obj = zf.ZipFile('comp_file.zip', 'r')
zip_obj.extractall("extracted_content")

# shutil.make_archive()   -> archive all files in a folder
# shutil.unpack_archive() -> extract all files in a folder
directory_to_zip = r'C:\Users\ponce\Documents\Personal\Healthcare'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', directory_to_zip)






# -----------------WORKING WITH IMAGES-----------------

# Open/save images
mac = Image.open('example.jpg')
mac.save("laptop.png")

# Image information
print(type(mac))
print(mac.size)
print(mac.filename)
print(mac.format_description)

# copy() -> copy the image to another image object
computer = mac.copy()

# paste(image1, image2, box, mask) -> paste an image on another image
# image1 is the image on which other image is to be pasted (optional)
# image2 is the original image
# box is a 4-tuple giving the region to paste into (optional)
# mask is an optional mask image
mac.paste(im=computer, box=(796, 0))

# crop((x,y,w,h)) -> return a rectangular region from an image
# x, y indicate the initial coordinate of the crop rectangle. They start at top corner (0,0)
# w, h indicate the width and height of the crop rectangle
# Start at top corner (0,0)
x = 0
y = 0
w = 1950/3
h = 1300/10
print(mac.crop((x, y, w, h)))

# resize((new_h,new_w)) -> method to resize an image
mac.resize((1000, 500))

# rotate() -> rotate a given image to the given number of degrees counter clockwise around its centre
# expand is optional and expands the output image to make it large enough to hold the entire rotated image
mac.rotate(90, expand=1)
