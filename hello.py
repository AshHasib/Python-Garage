
def isPrime(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, n):
            if n%i==0:
                return False
        return True

if __name__=='__main__':
    print('Hello welcome to python development env.')
    num=int(input('Enter a number:'))
    print('The number you have entered is '+ str(num))
    if isPrime(num)==True:
        if num is 2:
            print ('The number is prime and even')
        else:
            print ('The number is prime and odd')
    
    else:
        print ('The number is a non prime')
        
