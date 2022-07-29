import os
import sys
from loopnet import print_ll

print(os.chdir('D:\\Head_First_Python\\chapter3'))
print(os.getcwd())


# data = open('sketch.txt')
# # print(data.readline(),end='')
# # print(data.readline(),end='')


# for d in data:
#     if d.find(':') != -1:
#         (role, line) = d.split(':',1)
#         print(role, end='')
#         print(' said:', end='')
#         print(line,end='')
#     else:
#         continue


# data.close()

# if os.path.exists('sketch.txt'):
man = []
other = []
try:
    data = open('sketch.txt')
    for d in data:
        try:
            (role, line) = d.split(':',1)
            line = line.strip()
            if role == 'Man':
                man.append(line)
            elif role == 'Other Man':
                other.append(line)
        except Exception as er:
            print(er)

    data.close()
# else:
except Exception as er:
    print('Error message: ',er)

try:
    # PREV
    # man_f = open('man.txt','w') 
    # other_f = open('other.txt','w')
    # print(man,file=man_f) 
    # print(other,file=other_f)

    # with open('man.txt','w') as man_f:
    #     print(man,file=man_f)
    # with open('other.txt','w') as other_f:
    #     print(other,file=other_f)

    with open('man.txt','w') as man_f:
        # print_ll(man)
        print(man,file=man_f)
    with open('other.txt','w') as other_f:
        # print_ll(other)
        print(other,file=other_f)


    # OR
    # with open('man.txt','w') as man_f,     with open('other.txt','w') as other_f:
    #     print(man,file=man_f)
    #     print(other,file=other_f)
except Exception as er:
    print(er)
# finally:
#     man.close()
#     other.close()

