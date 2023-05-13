"""
COLLECTIONS
-Built-in module that implements specialized container data types.
-It provides alternatives to Python’s general purpose built-in containers.

Counter():
-dictionary subclass which helps count hashable objects.
-Elements are stored as dictionary keys and the counts of the objects are stored as the value.

defaultdict():
-defaultdict is a dictionary-like object but takes a first argument (default_factory) as a
default data type.
-if a key is not found in the dictionary, instead of a KeyError being thrown, a new entry will be
created.
-Using defaultdict is faster than doing the same using dict.set_default() method.

OrderedDict():
-OrderedDict is a dictionary subclass that remembers the order in which its contents are added.

namedtuple():
-A namedtuple assigns names, as well as the numerical index, to each member.
-The difference with standard tuple is that they only use numerical indexes.
-Each kind of namedtuple is represented by its own class, created by using the namedtuple()
factory function.
-The arguments are the name of the new class and a string containing the names of the elements.
"""

from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple



# -----------------COUNTER-----------------

# Counter() with lists
lst = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]
print(Counter(lst))
# output: Counter({1: 6, 2: 6, 3: 4, 12: 1, 32: 1, 21: 1, 223: 1})

# Counter() with strings
print(Counter('aabsbsbsbhshhbbsbs'))
# output: Counter({'a': 2, 'b': 7, 'h': 3, 's': 6})

# Counter() with words in a sentence
s = 'How many times does each word show up word times each each word'
words = s.split()
Counter(words)
"""
output: Counter({'How': 1, 'does': 1, 'each': 3, 'many': 1, 
                 'show': 1, 'times': 2, 'up': 1, 'word': 3})
"""

# most_common() -> return most common elements
c = Counter(words)
c.most_common(2)
# output: [('each', 3), ('word', 3)]

# Common patterns when using the Counter() object
# sum(c.values())              -> total of all counts
# c.clear()                    -> reset all counts
# list(c)                      -> list unique elements
# set(c)                       -> convert to a set
# dict(c)                      -> convert to a regular dictionary
# c.items()                    -> convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs)) -> convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]    -> n least common elements
# c += Counter()               -> remove zero and negative counts






# -----------------DEFAULTDICT-----------------

# Create a defaultdict()
# dict = defaultdict(datatype)
d = defaultdict(int)
d2 = defaultdict(object)

# defaultdict can also initialize with default values
d3 = defaultdict(lambda: 0)






# -----------------ORDEREDDICT-----------------

# Create OrderedDict() and adding elements to the dictionary
od = OrderedDict()
od['a'] = 'A'
od['b'] = 'B'
od['c'] = 'C'
od['d'] = 'D'






# -----------------NAMEDTUPLE-----------------

# Create namedtuple -> Subclass = namedtuple(object_type, 'field1 field2 ...')
Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')
frank = Dog(age=2, breed='Shepard', name="Frankie")
