		i += -1
		if i == 0:
			i = 8
		r = f.read(i)

for i in range(len(RAW_DATA)):
	l = len(RAW_DATA[i])
	tup = struct.unpack(TYPE[l], RAW_DATA[i])