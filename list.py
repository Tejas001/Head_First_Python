Python 3.9.11 (tags/v3.9.11:2de452f, Mar 16 2022, 14:33:45) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if 2 > 1:
	print('Worked')

	
Worked
>>> movie = ['Run','Thor','I']
>>> movie
['Run', 'Thor', 'I']
>>> type(movie)
<class 'list'>
>>> movie[1]
'Thor'
>>> len(movie)
3
>>> movie.append('pushpa')
>>> movie
['Run', 'Thor', 'I', 'pushpa']
>>> m = movie.pop()
>>> m
'pushpa'
>>> movie.extend(['Pushpa','Welcome'])
>>> movie
['Run', 'Thor', 'I', 'Pushpa', 'Welcome']
>>> movie.remove('Welcome')
>>> movie
['Run', 'Thor', 'I', 'Pushpa']
>>> movie.insert(0,'WallE')
>>> movie
['WallE', 'Run', 'Thor', 'I', 'Pushpa']
>>> movie.insert(1,1975)