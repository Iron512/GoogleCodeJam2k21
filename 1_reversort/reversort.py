#!/usr/bin/python

def debprint(arg):
	if debug:
		print(arg)

debug = 0

count = input()
for x in range(0,int(count)):
	useless = input()
	useful = input()
	candidate = [int(x) for x in useful.split(" ")]
	sol = 0

	pos = 0
	debprint(candidate)

	while pos < len(candidate)-1:
		find_number = 0
		while find_number+1 < len(candidate) and candidate[find_number] != pos+1:
			find_number+=1

		sol += find_number-pos+1

		#swap
		index_start = pos
		index_end = find_number
		for w in range(0,int((find_number-pos+1)/2)):
			tmp = candidate[index_start]
			candidate[index_start] = candidate[index_end]
			candidate[index_end] = tmp
			index_start+=1
			index_end-=1
			debprint(candidate)

		pos = pos+1
		debprint("")

	print("Case #" +str(x+1)+": " + str(sol))
