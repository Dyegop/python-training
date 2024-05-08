"""
The command line argument for the keyword is checked.
If the argument is saved, then the clipboard contents are saved to the keyword.
If the argument is list, then all the keywords are copied to the clipboard.
Otherwise, the text for the keyword will be copied to the clipboard.
This means the code will need to do the following:
"""

# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# sys.argv is a list in Python, which contains the command-line arguments passed to the script
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # Paste content from clipboard and save it to shelve object
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        # Copy all keywords to clipboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        # Copy keyword to clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
