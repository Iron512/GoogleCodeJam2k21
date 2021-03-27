#!/usr/bin/python

import sys

def debprint(arg):
	if debug:
		print(arg)

debug = 0

count = input()
constraints = count.split(" ")

tcon = int(constraints[0])
ncon = int(constraints[1])
qcon = int(constraints[2])

dec = 1

for tests in range(0,tcon):
	final = [1,2,3]

	if dec == -1:
		sys.exit()

	#track is ready
	#start with some questions

	print("1 2 3", flush = True)
	res = int(input())

	del final[res-1]
	final.insert(1,res)

	while (len(final) != ncon):
		new = len(final) + 1
		head = 0 
		tail = len(final) -1

		ans = new
		counter = 0
		while ans == new:
			print(str(new) + " " + str(final[head]) + " " + str(final[tail]), flush = True)
			ans = int(input())
			
			if ans == -1:
				sys.exit()


			if ans == new:
				if counter % 2 == 0 :
					if head+1 == tail:
						final.insert(head+1,new)
						ans = -1
					else:
						tail = tail-1
				else:
					if head+1 == tail:
						final.insert(head+1,new)
						ans = -1
					else:
						head = head+1

			counter +=1

		if ans == final[head]:
			final.insert(head,new)
		elif ans == final[tail]:
			final.insert(tail+1, new)

	for el in final:
		print(el, end=' ')
	print()

	dec = int(input())