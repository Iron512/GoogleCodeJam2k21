#!/usr/bin/python

def debprint(arg):
	if debug:
		print(arg)

debug = 0

count = input()
for x in range(0,int(count)):
	useful = input()
	candidate = useful.split(" ")
	
	xcost = int(candidate[0])
	ycost = int(candidate[1])
	candidate = [char for char in candidate[2]]
	
	sol = 0
	#1 - collapse question marks
	tormv = []

	debprint(candidate)

	sub = []
	skip = False
	for pos in range(0, len(candidate)):
		if candidate[pos] != "?":
			skip = False
			sub.append(candidate[pos])

	candidate = sub
	debprint(candidate)

	#2 - solution
	for pos in range(0, len(candidate)-1):
		examined = candidate[pos] + candidate[pos+1]

		if examined == "CJ":
			sol += xcost
		if examined == "JC":
			sol += ycost

	print("Case #" +str(x+1)+": " + str(sol))
