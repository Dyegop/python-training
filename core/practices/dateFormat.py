"""
Script to do the following:
  -It searches all the filenames in the current working directory for American-style dates.
  -When one is found, it renames the file with the month and day swapped to make it European-style.
"""

import re
import os
import shutil




datePattern = re.compile(r"""^(.*?)    # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)
path = 'C:\\Users\\ponce\\Downloads\\PyFolder\\'


def date_formatter(p_pattern, p_path):
    # Call os.listdir() to find all the files in the working directory
    for file in os.listdir(p_path):
        result = re.search(p_pattern, file)
        # Skip None results
        if result is None:
            continue
        # Save date parts
        before_date = result.group(1)
        month_part = result.group(2)
        day_part = result.group(4)
        year_part = result.group(6)
        after_part = result.group(8)
        # Renaming files
        file_renamed = before_date+day_part+'-'+month_part+'-'+year_part+after_part
        print(f'Renaming "{file}" to "{file_renamed}"...')
        shutil.move(p_path+file, p_path+file_renamed)


date_formatter(datePattern, path)














# TODO Loop over each filename, using the regex to check whether it has a date




# TODO If it has a date, rename the file with shutil.move()
