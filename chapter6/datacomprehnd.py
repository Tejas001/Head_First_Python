from enum import unique
import os

os.chdir('D:\Head_First_Python\chapter6')

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
            dc = {}
            r=r.readline().strip().split(',')
            return ({'name': r.pop(0),
            'dob':r.pop(0),
            'time': str(sorted(list(set([sanitize(i) for i in r])))[0:3])})
    except Exception as er:
        print(er)
        return None

# USing function
s = file_read('sarah2')
j = file_read('james2')
ju = file_read('julie2')
m = file_read('mikey2')

# Without using function
# with open('sarah.txt') as s:
#     s=s.readline().strip().split(',')
# with open('james.txt') as j:
#     j=j.readline().strip().split(',')
# with open('julie.txt') as ju:
#     ju=ju.readline().strip().split(',')
# with open('mikey.txt') as m:
#     m=m.readline().strip().split(',')

# sa = {}
# ja = {}
# jul = {}
# mi = {}

# (sa['s_name'],sa['s_dob'],sa['time']) = s.pop(0),s.pop(0),s
# (ja['j_name'],ja['j_dob'],ja['time']) = j.pop(0),j.pop(0),j
# (jul['ju_name'],jul['ju_dob'],jul['time']) = ju.pop(0),ju.pop(0),ju
# (mi['m_name'],mi['m_dob'],mi['time']) = m.pop(0),m.pop(0),m

# print(sa['s_name'] + "'s fastest times are: " +  str(sorted(list(set([sanitize(i) for i in sa['time']])))[0:3]))
# print(ja['j_name'] + "'s fastest times are: " +  str(sorted(list(set([sanitize(i) for i in ja['time']])))[0:3]))
# print(jul['ju_name'] + "'s fastest times are: " +  str(sorted(list(set([sanitize(i) for i in jul['time']])))[0:3]))
# print(mi['m_name'] + "'s fastest times are: " +  str(sorted(list(set([sanitize(i) for i in mi['time']])))[0:3]))

print(s['name'] + "'s fastest times are: " +  s['time'])
print(j['name'] + "'s fastest times are: " +  j['time'])
print(ju['name'] + "'s fastest times are: " +  ju['time'])
print(m['name'] + "'s fastest times are: " +  m['time'])