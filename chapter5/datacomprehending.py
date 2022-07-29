from enum import unique
import os

os.chdir('D:\Head_First_Python\chapter5')

def sanitize(time_string):
    """ This functions checks the mins and secs seperator 
    and remove other seperators in order to bring it in '.' format """
    if ':' in time_string:
        (mins,secs) = time_string.split(':')
    elif '-' in time_string:
        (mins,secs) = time_string.split('-')
    else:
        return time_string
    return mins+'.'+secs

def file_read(ft):
    try:
        with open(ft+'.txt') as r:
            r=r.readline().strip().split(',')
            return r
    except Exception as er:
        print(er)
        return None

# USing function
s = file_read('sarah')
j = file_read('james')
ju = file_read('julie')
m = file_read('mikey')

# Without using function
# with open('sarah.txt') as s:
#     s=s.readline().strip().split(',')
# with open('james.txt') as j:
#     j=j.readline().strip().split(',')
# with open('julie.txt') as ju:
#     ju=ju.readline().strip().split(',')
# with open('mikey.txt') as m:
#     m=m.readline().strip().split(',')

c_s = []
c_j = []
c_ju = []
c_m = []


c_s = sorted(list(set([sanitize(i) for i in s])))[0:3]
c_j = sorted(list(set([sanitize(i) for i in j])))[0:3]
c_ju = sorted(list(set([sanitize(i) for i in ju])))[0:3]
c_m = sorted(list(set([sanitize(i) for i in m])))[0:3]


# c_s.sort(),c_j.sort(),c_ju.sort(),c_m.sort()

print(c_s)
print(c_j)
print(c_ju)
print(c_m)