import pickle

man = ['Is this the right room for an argument?', "No you haven't!", 'When?', "No you didn't!", "You didn't!", 'You did not!', 'Ah! (taking out his wallet and paying) Just the five minutes.', 'You most certainly did not!', "Oh no you didn't!", "Oh no you didn't!", "Oh look, this isn't an argument!", "No it isn't!", "It's just contradiction!", 'It IS!', 'You just contradicted me!', 'You DID!', 'You did just then!', '(exasperated) Oh, this is futile!!', 'Yes it is!']
other = ["I've told you once.", 'Yes I have.', 'Just now.', 'Yes I did!', "I'm telling you, I did!", "Oh I'm sorry, is this a five minute argument, or the full half hour?", 'Just the five minutes. Thank you.', 'Anyway, I did.', "Now let's get one thing quite clear: I most definitely told you!", 'Oh yes I did!', 'Oh yes I did!', 'Yes it is!', "No it isn't!", 'It is NOT!', "No I didn't!", 'No no no!', 'Nonsense!', "No it isn't!"]

try:
    with open('my_data.pickle','wb') as my_d:
        pickle.dump([1,2,3,4],my_d)

    with open('my_data.pickle','rb') as my_r:
        l = pickle.load(my_r)

    print(l)
except Exception as er:
    print(er)

try:
    with open('man1.txt','wb') as my_man:
        pickle.dump(man,my_man)

    with open('other1.txt','wb') as my_other:
        pickle.dump(other,my_other)

except Exception as er:
    print(er)