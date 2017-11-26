if __name__=='__main__':
	str='\nHi this is an edit\n'

	appender=open('Sample.txt','a')
	appender.write(str)
	appender.close()