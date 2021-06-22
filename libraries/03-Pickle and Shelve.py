"""
PICKLE
-An alternativefor serializing and de-serializing a Python object structure.
-By "serialize" we mean convert it from a python object into a string (pickling) in a way that it can be turned back into
an equivalent python object later (unpickling).
-Pickle has the strength that it can serialize nearly anything but one of the downsides of pickle is that someone
could engineer a pickle file with malicious code in it.

SHELVE
-Shelve module provides an easier way to load and save from a pickle file
"""

import pickle
import shelve




# -----------------PICKLE-----------------

# Initialize data to be stored in db
Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}
Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}

# Create dictionary object and add data
db = {'Omkar': Omkar, 'Jagdish': Jagdish}

# Create pickle
# It is important to use binary mode (ab = append binary)
dbfile = open('examplePickle.pkl', 'ab')

# Store data
# Source is a dictionary object, destination will be a pickle
pickle.dump(db, dbfile)
dbfile.close()

# Function to load data
def load_data():
    # Open pickle object
    # For reading also binary mode is important
    load_file = open('examplePickle.pkl', 'rb')
    # Load data from pickle object
    load_db = pickle.load(load_file)
    # Print data
    for keys in load_db:
        print(keys, '=>', load_db[keys])
    load_file.close()






# -----------------SHELVE-----------------

# Using shelve module to load and save data
examplePickle = shelve.open('examplePickle.pkl')

# Add data to pickle object
examplePickle['Omkar'] = 1235

# Save the file
examplePickle.close()