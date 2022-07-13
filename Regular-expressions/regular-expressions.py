"""
    Module Regular expressions specifies a set of string patterns that matches it. 
    There are a total of 14 metaCharacters:

    1. \ - used to drop the special meaning of the character following it
    2. [] - Represent a character class
    3. ^ - Matches the beginning
    4. $ - Matches the end
    5. . - Matches any character except the new line
    6. ? - Matches zero or one occurrence
    7. | - or. Matches any of the characters on any side of it
    8. * - any number of occurrences, including zero
    9. + - one or more occurrences
    10. {} - indicate the number of occurrences of a preceding RE to match
    11. () - Enclose a group of REs

    The most common methods include:

"""
from mailcap import findmatch
import re


string = " Hello, my number is 073844458899998874799"

"""
        \d - matches any decimal digit
        \D - matches any non-decimal digit
        \s - matches any whitespace character
        \S - matches any non-whitespace character 
        \w - matches any alphanumeric character [a-zA-Z0-9_]
        \W - matches any non-alphanumeric character
"""
regex = '\d+'

"""return all non-overlapping matches of pattern in string, as a list of strings. the string is 
    scanned left to right, and matches are returned in the order found.
"""
print(re.findall(regex, string))

"""compile() compiles regular expressions into pattern objects which have methods for various operations like 
    searching for pattern matches or string substitutions
"""
p = re.compile('[0-5]')
print(p.findall(string))

"""
    re.match() tries to match a pattern to a whole string. It returns a match object on success, and a None on failure.

"""

def findMonthAndDate(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.match(regex, string)
    if match == None:
        print("Invalid date")
        return
    print("Given string: ", match.group())
    print("Month: ", match.group(1))
    print("Day: ", match.group(2))

findMonthAndDate("July 20 1996")

"""
    re.search() returns None if pattern doesn't match or a re.MatchObject that contains information about the matching part of 
    the string. 

"""

def findMatch(string):
    regex = r"([a-zA-Z]+) (\d+)"
    match = re.search(regex, string)
    if match != None:
        print("Match at index %s, %s"%(match.start(), match.end()))
        print("Full match: %s " %(match.group(0)))
        print("Month: %s"%(match.group(1)))
        print("Day: %s "%(match.group(2)))
    else:
        print("The regex pattern does not match")

findMatch("The date is July 56")


"""
    we can use re.split() to split a string by the occurrence of a character or pattern and upon finding that pattern, 
    the remaining charactes from the string are returned as part of the resulting list
"""
def splitString(string):
    regex = '\W+'
    print(re.split(regex, string))
    pass
splitString("My name is Lenny Weda")
