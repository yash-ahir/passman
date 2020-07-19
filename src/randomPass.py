import string
from random import shuffle
from secrets import choice

def generatePass(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)
    shuffle(chars)
    password = ""
    for i in range(0, length):
        password += choice(chars)
    return password