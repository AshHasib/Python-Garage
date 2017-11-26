if __name__=='__main__':
	str='Hello This is the first line\n to be written in a text file'
	saveFile = open('Sample.txt', 'w')
	saveFile.write(str)
	print('task complete')
	saveFile.close()