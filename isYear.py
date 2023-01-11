def legalYear(word):
	flag = False
	for i in range(len(word)-1):
		if not 'א' <= word[i] <= 'ת':
			return False
		if word[i] != 'ת':
			if val(word[i+1]) >= val(word[i]):
				if not flag:
					flag = True
				else:
					return False
	return 'א' <= word[len(word)-1] <= 'ת'
def val(c):
	if 'א' <= c <= 'ט':
		return 0
	elif 'י' <= c <= 'צ':
		return 1
	elif 'ק' <= c <= 'ת':
		return 2
	else:
		return -1


f = open("hebrew.txt", "r")

for line in f:
	for word in line.split():
		if legalYear(word):
			print(word + "\n")
