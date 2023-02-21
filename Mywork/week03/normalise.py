# normalise.py
# This program reads in a string and strips any leading or trailing spaces, also convert the string to lower case

rawString = input ("please enter a string")
normalisedString = rawString .strip () .lower ()

lenghtOfRawString = len (rawString)
lenghtOfNormalised = len (normalisedString)
print (f"That string normalised is: {normalisedString}")
print (f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")
