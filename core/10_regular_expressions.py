"""
REGULAR EXPRESSIONS:
-Regular expressions are text-matching patterns described with a formal syntax.
-Regular expressions are often referred to as `regex`.
-Regular expressions support a huge variety of patterns
"""

import re



# -----------------SEARCHING PATTERNS-----------------

patterns = ['term1', 'term2']
text = 'This is a string with term1, but it does not have the other term.'
text2 = 'What is the domain name of someone with the email: hello@gmail.com'
text3 = "my phone is a new phone"

# re.search(pattern, text) -> search patterns in a text
# This function returns None if no pattern is found
for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' % (pattern, text))
    if re.search(pattern, text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

# re.findall(pattern, text) -> find all patterns in a text
# Use a . (wildcard) as a placement that will match any character placed there
re.findall('match', 'test phrase match is in middle')
re.findall(r'.at', 'The cat in the hat sat here')

# re.finditer(match, text) -> return an iterator yielding actual match objects
for match in re.finditer("phone", text3):
    print(match.span())

# match() -> determine if the regular expression matches at the beginning of the string
re.match('This', text)

# re.compile(pattern) -> compile a regular expression pattern into a regular expression object
# This object can be used in methods, like match(), find(), findall(), search()
re.findall(re.compile('is*'), text)

# re.split(split_condition, text) -> split a text based on condition
split_term = '@'
re.split(split_term, text2)

# group(n) -> return the string matched by the regular expression
# group function internally set numbers to different parts of the regular expression
# n -> optional parameter, return n part of the matched string
match = re.compile(r'^(.*?)([0123])?\d-([01])?\d-((19|20)\d\d)$')
text4 = 'Current date: 23-09-2020'
result = re.search(match, text4)
print(result.group(1))  # Output: 'Current date: '
print(result.group(2))  # Output: '23'
print(result.group(4))  # Output: '09'
print(result.group(6))  # Output: '2020'


# start() -> return the starting position of the match
# end()   -> return the ending position of the match
# span()  -> return a tuple containing the (start, end) positions of the match
match2 = re.match('This', text)
print(match2.start(), match2.end())
print(match2.span())

# re.VERBOSE    -> allow you to write regular expressions that look more readable
# re.IGNORECASE -> perform case-insensitive matching, ignoring uppercase and lowercase matching
# You can visually separate logical sections of the pattern and add comments
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.VERBOSE)






# -----------------PATTERNS-----------------

# Metacharacters with regular expressions:
# [] -> specify character class, a set or range of characters to match. Metacharacters are not
# active inside []
# () -> group part of the regular expression together
# .  -> any character except newline
# ^  -> start of string. If inside [], exclude characters (for example, [^1-9])
# $  -> end of string
# \  -> escape all the metacharacters, so you can still match them in patterns
# |  -> or operator to indicates several conditions
# *  -> specify that the previous character can be matched zero or more times
# +  -> specify that the previous character can be matched one or more times
# ?  -> specify that the previous character can be matched zero or one time
# {} -> specify a set or range of repetitions
# syntax: {m, n}, where m is the minimum number of repetitions and n is the maximum. You can
# omit either m or n

# Special sequencies with \
# \d -> match any decimal digit; equivalent to the class [0-9]
# \D -> match any non-digit character; equivalent to the class [^0-9]
# \s -> match any whitespace character; equivalent to the class [ \t\n\r\f\v]
# \S -> match any non-whitespace character; equivalent to the class [^ \t\n\r\f\v]
# \w -> match any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]
# \W -> match any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]


# Example 1:
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['sd*',      # s followed by zero or more d's
                 'sd+',      # s followed by one or more d's
                 'sd?',      # s followed by zero or one d's
                 'sd{3}',    # s followed by three d's
                 'sd{2,3}',  # s followed by two to three d's
                 '[sd]',     # either s or d
                 's[sd]+'    # s followed by one or more s or d
                 ]

def multi_re_find(v_patterns, v_phrase):
    for my_pattern in v_patterns:
        print(re.findall(my_pattern, v_phrase))
        print('\n')
multi_re_find(test_patterns, test_phrase)


# Example 2:
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
re.findall('[^!.? ]+', test_phrase)


# Example 3:
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'
test_patterns = ['[a-z]+',       # sequences of lower case letters
                 '[A-Z]+',       # sequences of upper case letters
                 '[a-zA-Z]+',    # sequences of lower or upper case letters
                 '[A-Z][a-z]+']  # one upper case letter followed by lower case letters
multi_re_find(test_patterns, test_phrase)

# Example 4: Using () and [] to create subpatterns
# Main pattern: [a-zA-Z0-9.]+(@[a-zA-Z.]+\.[a-zA-Z]{2,4})
# Subpattern: (@[a-zA-Z.]+\.[a-zA-Z]{2,4})
email_list = [
    'yamla@optonline.net', 'smallpaul@comcast.net', 'esokullu@yahoo.com', 'dkeeler@gmail.com'
]
pattern = re.compile(r'([a-zA-Z0-9.]+(@[a-zA-Z.]+\.[a-zA-Z]{2,4}))')
