# from nester import loopnet

# print(loopnet.print_ll(man,f=man))
import loopnet
import pickle

data= []

try:
    with open('man1.txt','rb') as my_man:
        data = pickle.load(my_man)
except Exception as er:
    print(er)
finally:
    print('***********The End********')
loopnet.print_ll(data)