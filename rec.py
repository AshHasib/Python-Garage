def rec(n):
	if(n>=20):
		return
	else:
		rec(n+1)
		print(n)
		
if __name__=='__main__':
rec(1)