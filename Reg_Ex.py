# Regular Expressions
""""
The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
"""


import re


mystr = """My name is samrat.
i study in grade 12.
i am 18 yrs old.
i like coding.
i love sports mainly Basketball and Football"""

# findall, search, split, sub, finditer

#finditer
patt = re.compile(r"like")
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print(mystr[59:63])
print()

patt = re.compile(r".rat")
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()

# My bata start bhako bhara "^" yo use garni
patt = re.compile(r'^My')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()

# Football. ma end bhako bhayera '$' use garni
patt = re.compile(r'Football$')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()

# *
patt = re.compile(r'ai*')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()

# +
patt = re.compile(r'ai+')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()

# {}
patt = re.compile(r'ai{1}')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()

# ()
patt = re.compile(r'(ai){1}')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()

# |
patt = re.compile(r'ai{1}|yrs')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print()


# Special Sequences
patt = re.compile(r'\bsamrat.')

