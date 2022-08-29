	RAW_DATA[i] = abs(sum(list(tup)))

for i in range(0,len(RAW_DATA),2):
	LETTERS.append(RAW_DATA[i] % RAW_DATA[i+1])

print "The solution is...",
print chr(LETTERS[0] % 884 + 60),
print chr(LETTERS[1] % 2908 + 29),
print chr(LETTERS[2] % 2988 + 60),
print chr(LETTERS[3] + 75),
print chr(LETTERS[4] % 3330 - 5),
print chr(LETTERS[5] % 270 - 36)