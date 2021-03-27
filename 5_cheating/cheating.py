#!/usr/bin/python

def debprint(arg):
	if debug:
		print(arg)

partCount = 100
count = int(input())
useless = input()

debug = 1

for times in range(0, count):
	partecipants = []
	for x in range(0, partCount):
		answers = input()
		
		tot = 0
		partecipants.append([])
		for val in answers:
			tot += int(val)
			partecipants[x].append(int(val))

		partecipants[x].insert(0,tot)

	partecipants = sorted(partecipants, reverse = True)
	partecipants = partecipants[0:25]
	for x in range(0,len(partecipants)):
		debprint(str(x+1) + " " + str(partecipants[x][0]))

	#partecipant contains the top 25% people, which should have at least 1.5 of skill
	#We can expect them to have some answer which they all answered correctly, the cheater could have failed some

	resume = []
	resume.append(100)

	for x in range(1,len(partecipants[0])):
		resume.append(0)
		for y in range(0,len(partecipants)):
			resume[x] += partecipants[y][x]

	partecipantsErrors = []

	for x in range(0,len(partecipants)):
		partecipantsErrors.append(0)

	print(min(resume))
	print([x for x,y in enumerate(resume) if y == min(resume)])

	for x in range(1,len(resume)):
		if resume[x] == 24 or resume[x] == 23 or resume[x] == 22:
			for y in range(0,len(partecipants)):
				if (partecipants[y][x] == 0):
					partecipantsErrors[y] += 1

	print(partecipantsErrors)


	print("Case #" + str(times+1) + ": ",end="")
	print()
