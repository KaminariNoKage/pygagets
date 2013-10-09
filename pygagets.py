"""
PY GAGETS
BY KAI AUSTIN
A various assortment of functions related to basic puzzle games, crypts, etc.
Others may find these functions useful as well
AUGUST 2013
"""
import random

def substr_split(message, subleng, ignore_spaces = False):
    """
    RETURNS LIST
        Splits a string into a list comprised of substrings
        of whatever the length specificed.
    message = the string to be split into the list
    subleng = the length of the substring to be included
    ignore_spaces = boolean, determines whether to ignore punctuation or not
    """
    sublist = []
    #Removes spaces if spacing is ignored
    if ignore_spaces:
        message = message.replace(' ', '')
    #splits the string into the list
    while len(message) > 0:
        sublist.append(message[:subleng])
        message = message[subleng:]
    
    return sublist

def remove_punc(message):
    """
    RETURNS STRING
        Removes all the punctuation in a string
    message = the string to remove all punctuation from
    """
    depunc = ''
    for el in message:
        if 47 <= ord(el) <= 57 or 65 <= ord(el) <= 90 or 97 <= ord(el) <= 122:
            depunc += el
    return depunc

def scramble(word):
    '''
    RETURNS STRING
        Takes in a word (or any string) and randomizes the characters it contains
    word = string of characters
    '''
    letter_split = []
    for character in word:
        letter_split.append(character)
    
    randomized = ''
    
    while len(letter_split) >= 1:
        letter_pos = random.randint(0,len(letter_split)-1)
        randomized = randomized + letter_split.pop(letter_pos)
        
    return randomized


def shift(message, offset):
    """
    RETURNS STRING
        Takes in a message and applies ceasar encryption (shift)
        Each letter is pushed forward by the offset letter in the alphabet
        For example, "cat" with an offset "2" becomes "ecv"
        Capitalization and spaces are maintained.
    message = STRING with the message to be changed
    offset = INT (+/-) indicating the offset number
    """
    crypt = ''
    acap = 65 
    zcap = 90 
    alow = 97 
    zlow = 122
    #In the event offset is negative
    if offset < 0:
        offset += 26
        
    for el in message:
        #Converting letter to int form and applying offset
        tonum = ord(el)
        #If capital letters
        if acap <= tonum <= zcap:
            tonum += offset
            if tonum > zcap:
                crypt += chr(tonum - zcap + acap - 1)
            else:
                crypt += chr(tonum)
        #If lowercase letters
        elif alow <= tonum <= zlow:
            #adjusting the range to 0-25
            tonum += offset
            if tonum > zlow:
                crypt += chr(tonum - zlow + alow - 1)
            else:
                crypt += chr(tonum)
        else:
            crypt += el
        
    return crypt

def alpha_shift(message):
    """
    RETURNS LIST
        Takes in a message and applies shift() for the entire alphabet
        and provides all possible variations of the string with an
        encrypted alphabet, except the original message
    message = string
    """
    alpha_list = []
    for i in range(25):
        i += 1
        alpha_list.append(shift(message,i))
    return alpha_list
    
    
def num_encrypt(message, offset=0, digits=2):
    """
    RETURNS STRING
        Takes in a message (with optional offset) and applies number
        encryption for it. Where A/a = 01, B/b = 02, etc.
    message = string desired for encryption
    offset = OPTIONAL, a positive integer to offset the starting number (eg: offset = 3, A = 04)
    digits = OPTIONAl, a positive integer >= 2 denotting the number of digits 
        to represent each letter (eg: digits = 3, A = 001)
    """  
    message = message.upper() #because who likes little letters?
    crypt = ''
    ord_adjust = 65 - 1
    for el in message:
        #Convert to number string form and add to pending list
        if 65 <= ord(el) <= 90:
            numbified = str(ord(el) - ord_adjust + offset)
            if len(numbified) > digits or digits < 2:
                print "The numbers do not fit in your digit constaint."
                print "Please enter a new digit value, equal or greater than 2, and try again."
                break
            else:
                while len(numbified) != digits:
                    numbified = '0' + numbified
                crypt += numbified
        else:
            crypt += el
    
    return crypt
    

def num_decrypt(message, offset=0, digits=2):
    """
    RETURNS STRING
        Takes in a message (with optional offset) and applies number
        encryption for it. Where A/a = 01, B/b = 02, etc.
        WARNING: Do not use with punctuation
    message = string desired for encryption
    offset = OPTIONAL, a positive integer to offset the starting number (eg: offset = 2, 03 = A)
    digits = OPTIONAl, a positive integer denotting the number of digits 
        to represent each letter (eg: digits = 3, 001 = A)
    """
    decrypt = ''
    message = remove_punc(message) #removing punctuation as interfers with splitstr()
    splitstr = substr_split(message, digits, True)
    for num in splitstr:
        decrypt += chr(int(num) + 64)
    return decrypt

ms = raw_input("Insert message here: ")
print num_encrypt(ms, 13)

def print_list(strlist, location = 'console', filename = 'newfile.txt', filetodo = 'w'):
    """
    PRINTS STRING
        Prints each element of strlist to the specified location
        one line per index
    strlist = array of strings with message to print
    location = string, where the list will be printed to
    filename = string, the name of the file where to write things
    filetodo = string, write/overwrite file (w) or append to existing one (a)
    """
    if location == 'console':
        for str in strlist:
            print str
    elif location == 'file' or location == 'txt':
        name = filename
        f = open(name, filetodo)
        for str in strlist:
            f.write(str)
    else:
        print 'Cannot write file'
        print 'Possible locations are: console, file (or txt)'

def stringify(item):
    """
    RETURNS STRING
        Turns a Tuple, Int, and List into a string
    item = any type, whatever to be converted into string
    """
    if isinstance(item, str):
        #If a string
        return item
    elif isinstance(item, int):
        #If an integer
        return str(item)
    elif isinstance(item, list):
        #if a list
        templist = []
        for i in item:
            templist.append(stringify(i))
        return '[' + ','.join(templist) + ']'
    elif isinstance(item, tuple):
        #if a tuple
        templist = []
        for i in item:
            templist.append(stringify(i))
        return '(' + ','.join(templist) + ')'
    else:
        return '<unknown>'

def print_dict(dictlist, location = 'console', filename = 'newfile.txt', filetodo = 'w'):
    """
    PRINTS STRING
        Prints each element of a dictionary to the specified location
        one line per key : value
    dictlist = dictionary with message to print
    location = string, where the list will be printed to
    filename = string, the name of the file where to write things
    filetodo = string, write/overwrite file (w) or append to existing one (a)
    """
    if location == 'console':
        for key in dictlist:
            print stringify(key) + ' : ' + stringify(dictlist[key])
    elif location == 'file' or location == 'txt':
        name = filename
        f = open(name, filetodo)
        for str in strlist:
            f.write(str)
    else:
        print 'Cannot write file'
        print 'Possible locations are: console, file (or txt)'



print scramble("elementary")