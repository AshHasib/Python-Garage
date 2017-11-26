def fibonacci(upto):
	f1=0
	f2=1
	nextf=f1=f2
	while(nextf<=upto):
		print(nextf),
		f1=f2
		f2=nextf
		nextf=f1+f2


num=int(input('Enter a number:'))
fibonacci(num)