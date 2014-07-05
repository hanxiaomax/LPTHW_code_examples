def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return Error 

from sys import argv
script,num=argv

print convert_number(num)