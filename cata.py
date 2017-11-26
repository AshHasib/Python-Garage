
def cata(x):
	str_x=str(x)
	start=0

	for element in str_x:
		start+=int(element)

	return start

print(cata(12345)) 