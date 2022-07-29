class nested_lis(list):

    def __init__(self,l_name):
        list.__init__([])
        self.name = l_name

t = nested_lis('Tejas Chougule')
# print(t.name)
print(dir(t))
t.append('Sagar Bhalke')
t.extend(['Divesh Kubal','Milind Kubal'])
print(t)

for i in t:
    print('Players name: ',i)