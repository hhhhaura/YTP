from Puzcopan import *
dir = input('Please input the directory of your images\n')
num = int(input('Please input the number of images you have\n'))
for i in range(1, num + 1) : 
	print(i)
	image(dir + str(i) + '.png')
cur = 0
slot = 0
component(0)
while True : 
	print('cur piece', cur)
	yes = input('is it done ? \n')
	if yes == "done" :
		component(0)
	solve(slot)
	next()
	x = input('ok?\n')
	if x == "skip" :
		slot += 1
		continue
	while x != 'ok':
		next()
		x = input('ok?\n')

	ok()
	slot += 1
	



