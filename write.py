if __name__=='__main__':

	str='Printing from 1 to 100\n'

	writeFile=open('Print.txt','w')
	writeFile.write(str)
	for i in range(1,100+1):
		print(i)
		writeFile.write(i)
		if(i%10)==0:
			print("")

	writeFile.close()