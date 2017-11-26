def isPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    else:
        for i in range(3,n,2):
            if n%i==0:
                return False
                break
        return True

if __name__=='__main__':
    L=[]
    num=int(input('Enter range:'))
    for i in range (2,num+1):
        if isPrime(i)==True:
            L.append(i)
    print('Prime numbers:')
    for i in L:
        print(i)

