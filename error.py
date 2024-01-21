'''
Detect the legality of the string
'''

def isValidChar(text : str):
    return (ord('a') <= ord(text) and ord(text) <= ord('z')) or \
           (ord('A') <= ord(text) and ord(text) <= ord('Z')) or \
           (ord('0') <= ord(text) and ord(text) <= ord('9')) or \
           (text in ['(', ')', '|', '*', '.'])

def isValidStr(text : str):
    if (len(text) == 0):
        return False
    for char in text:
        if not isValidChar(char):
            return False
    return True

def isClosed(text : str):
    count = 0
    for char in text:
        if char == '(':
            count = count + 1
        elif char == ')':
            count = count - 1
    return (count == 0)

def isChar(text : str):
    return (ord('a') <= ord(text) and ord(text) <= ord('z')) or \
           (ord('A') <= ord(text) and ord(text) <= ord('Z')) or \
           (ord('0') <= ord(text) and ord(text) <= ord('9')) or \
           (text == '.') 