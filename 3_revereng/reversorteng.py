#!/usr/bin/python

def debprint(arg):
	if debug:
		print(arg)

def maxcount(number):
	return int(((number+1)*number)/2)

def swap(arr, start, end):
	for x in range(0,int(((end-start)+1)/2)):
		tmp = arr[end]
		arr[end] = arr[start]
		arr[start] = tmp

		start+=1
		end-=1

debug = 0

count = input()
for x in range(0,int(count)):
	useful = input()
	candidate = useful.split(" ")

	nco = int(candidate[0])
	step = int(candidate[1])

	sol = "IMPOSSIBLE"

	if not (step < nco-1 or step > maxcount(nco)-1):
		actual = nco-1
		final = []

		for y in range(0,nco):
			final.append(y+1)

		progression = 0
		start = 0
		end = len(final)-1
		while(actual != step):
			#solve
			if (step - actual <= end-start):
				disp = step - actual
				end = start + disp

			swap(final, start, end)
			step += (start-end)

			if progression % 2 == 0:
				end-=1
			else:
				start+=1

			progression +=1
			

		sol = ""
		for y in range(0,nco):
			sol += str(final[y]) + " "

	print("Case #" +str(x+1)+": " + str(sol))
