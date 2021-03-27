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
		else:
			if not skip:
				skip = True
				sub.append("?")

	candidate = sub
	debprint(candidate)

	#2 - solution
	for pos in range(0, len(candidate)-1):
		examined = candidate[pos] + candidate[pos+1]

		if examined == "CJ":
			sol += xcost
		if examined == "JC":
			sol += ycost

		if candidate[pos] == "?":
			#if the position is 0, we can copy the next symbol and pay nothing
			if pos != 0:
				#if the position is in the middle, but the corner of the question mark
				#are identical we copy the symbol and pay nothing
				if (candidate[pos-1] != candidate[pos+1]) and candidate[pos-1] == "C":
					sol += xcost
				else:
					sol += ycost

	print("Case #" +str(x+1)+": " + str(sol))
