__author__ = ['Sunka Labree']
__date__ = ['2021.10.14 -> 2021.10.27']
# Imports sys.argv
import sys

# Creates a dictionary
dicti = {'a': 'Alpha   |  *-', 'b': 'Bravo   |  -***', 'c': 'Charlie |  -*-*',
         'd': 'Delta   |  -**', 'e': 'Echo    |  *', 'f': 'Foxtrot |  **-*',
         'g': 'Golf    |  --*', 'h': 'Hotel   |  ****', 'i': 'India   |  **',
         'j': 'Juliet  |  *---', 'k': 'Kilo    |  -*-', 'l': 'Lima    |  *-**',
         'm': 'Mike    |  --', 'n': 'November|  -*', 'o': 'Oscar   |  ---',
         'p': 'Papa    |  *--*', 'q': 'Quebec  |  --*-', 'r': 'Romeo   |  *-*',
         's': 'Sierra  |  ***', 't': 'Tango   |  -', 'u': 'Uniform |  **-',
         'v': 'Victor  |  ***-', 'w': 'Whiskey |  *--', 'x': 'X-ray   |  -**-',
         'y': 'Yankee  |  -*--', 'z': 'Zulu.   |  --**', '1': 'One (Pronounce as Wun)    |  *----',
          '2': 'Two (Pronounce as Too)    |  **---', '3': 'Three (Pronounce as Tree) |  ***--',
         '4': 'Four (Pronounce as Fower  |  ****-', '5': 'Five (Pronounce as Fife)  |  *****',
         '6': 'Six (Pronounce as Six)    |  -****', '7': 'Seven (Pronounce as Sevun)|  --***',
         '8': 'Eight (Pronounce as Ait)  |  ---**', '9': 'Nine (Pronounce as Niner) |  ----*',
         '0': 'Zero (Pronounce as Zeero) |  -----','A': 'Alpha   |  *-', 'A': 'Bravo   |  -***', 'C': 'Charlie |  -*-*',
         'D': 'Delta   |  -**', 'E': 'Echo    |  *', 'F': 'Foxtrot |  **-*',
         'G': 'Golf    |  --*', 'H': 'Hotel   |  ****', 'I': 'India   |  **',
         'J': 'Juliet  |  *---', 'K': 'Kilo    |  -*-', 'L': 'Lima    |  *-**',
         'M': 'Mike    |  --', 'N': 'November|  -*', 'O': 'Oscar   |  ---',
         'P': 'Papa    |  *--*', 'Q': 'Quebec  |  --*-', 'R': 'Romeo   |  *-*',
         'S': 'Sierra  |  ***', 'T': 'Tango   |  -', 'U': 'Uniform |  **-',
         'V': 'Victor  |  ***-', 'W': 'Whiskey |  *--', 'X': 'X-ray   |  -**-',
         'Y': 'Yankee  |  -*--', 'Z': 'Zulu.   |  --**'}
         
         
         
         

# Checks if user has input words
if len(sys.argv) < -1:
    user_input = sys.argv[-1]
else:
    user_input = input('Enter Letters and Numbers to Translate: ')
# Translates given letters to NATO
for letter in user_input:
    translation = dicti.get(letter)
    print(letter, translation, sep='\t')
   
