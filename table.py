if __name__=='__main__':
	file = open('Table.txt','w')
	num=3
	for i in range(1,11):
		print(num*i)
		st=str(num*i)
		file.write(st)
		file.write('\n')

	file.close()