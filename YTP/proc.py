from Puzcopan import *
dir = input('Please input the directory of your images\n')
num = int(input('Please input the number of images you have\n'))
for i in range(1, num + 1) : 
	image(dir + str(i) + '.png')
while True : 
	tp = input('Operation\n c : component\n s : solve slot\n n : next\n nn : now\n l : last\n ok : ok\n\n')
	if tp == 'c': 
		x = input('component id\n')
		while not x.isdigit():
			x = input('try again.\n component id\n')
		x = int(x)
		component(x)
	elif tp == 's' : 
		x = input('slot id\n')
		while not x.isdigit():
			x = input('try again.\n slot id\n')
		x = int(x)
		solve(x)
	elif tp == 'n' :
		next()
	elif tp == 'nn' :
		now()
	elif tp == 'l' :
		last()
	elif tp == 'ok':
		ok()
	elif tp == 'done':
		print('Congrats! And Bye Bye\n')
		exit(0)
	else :
		print('not a command.\n try again.\n')



