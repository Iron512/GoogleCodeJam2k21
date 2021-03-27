#!/usr/bin/python

import sys

count = input()
constraints = count.split(" ")

tcon = int(constraints[0])
ncon = int(constraints[1])
qcon = int(constraints[2])

for tests in range(0,tcon):
	final = [1,2,3]

	print("1 2 3", flush = True)
	res = int(input())

	if res == -1:
		sys.exit(1)

	del final[res-1]
	final.insert(1,res)

	while (len(final) != ncon):
		new = len(final) + 1
		head = 0 
		tail = len(final) -1

		print(str(new) + " " + str(final[head]) + " " + str(final[tail]), flush = True)
		ans = int(input())

		if ans == new:
			#dicotomica
			while head != tail-1:
				middle = int((head + tail)/2)
				print(str(new) + " " + str(final[head]) + " " + str(final[middle]), flush = True)
				ans = int(input())

				if ans == -1:
					sys.exit(1)

				if ans == new:
					tail = middle
				else:
					head = middle

			#found, between tail and head
			final.insert(tail, new)
		elif ans == final[head]:
			final.insert(head, new)
		elif ans == final[tail]:
			final.insert(tail+1, new)
		elif ans == -1:
			sys.exit(1)

	for el in final:
		print(el, end=' ')
	print()

	dec = int(input())
	if dec == -1:
		sys.exit(0)