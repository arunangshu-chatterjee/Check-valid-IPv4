def is_valid_IP(strng):
	try:
		x = [i for i in strng.split('.')]
		for item in x:
			if int(item) < 0 or int(item) > 255:
				return False
		if len(x) == 4:
			for i in range(0,len(x)):
				if len(str(x[i])) > 3 or (len(str(int(x[i]))) != len(str(x[i]))):
					return False
				elif len(str(x[i])) > 1 and str(x[i])[0]=='0':
					return False
			return True
		return False
	except ValueError as e:
		return False