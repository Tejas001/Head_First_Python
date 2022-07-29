import os

os.chdir('D:\Head_First_Python\chapter6')
# class Athlete:
#     def __init__(self, value=0):
#         self.thing = value
#     def how_big(self):
#         return(len(self.thing))

# d = Athlete('Tejas')
# print(d.how_big())

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

class Athlete:

    def __init__(self,name,dob=None,time=[]) :
        self.name = name
        self.dob = dob
        self.time = time

    def top3(self):
        return( sorted(set([sanitize(i) for i in self.time]))[0:3])

    def add_time(self,time_value):
        return self.time.append(time_value)

    def add_times(self,time_val_list):
        return self.time.extend(time_val_list)

def file_read(ft):
    try:
        with open(ft+'.txt') as r:
            r=r.readline().strip().split(',')
            return (Athlete(r.pop(0),r.pop(0),r))
    except Exception as er:
        print(er)
        return None

s = file_read('sarah2')
j = file_read('james2')
ju = file_read('julie2')
m = file_read('mikey2')

print(s.time)

print(s.name + "'s fastest times are: " +  str(s.top3()))
print(j.name + "'s fastest times are: " +  str(j.top3()))
print(ju.name + "'s fastest times are: " +  str(ju.top3()))
print(m.name + "'s fastest times are: " +  str(m.top3()))

t = Athlete('Sagar')
t.add_time(1.05)
print(t.time)
# print(type(s.time))
# print(s.name)
# print(s.top3())

# Inherit
class AthleteList(list):

    def __init__(self,name,dob=None,time=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.time = time
    
    def top3(self):
        return( sorted(set([sanitize(i) for i in self.time]))[0:3])

t = AthleteList('Tejas C')
print(t.name)
t.append('Sagar')
print(t)
# Tejas_DataScience