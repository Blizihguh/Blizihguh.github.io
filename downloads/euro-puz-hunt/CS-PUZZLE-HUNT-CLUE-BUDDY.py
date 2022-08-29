	3: "Hb",
	2: "h",
	1: "b"
}

with open("CS-PUZZLE-HUNT-CLUE.bin", "rb") as f:
	i = 8
	r = f.read(i)
	while r:
		RAW_DATA.append(r)