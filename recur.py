

def fib(n=0):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

if __name__=='__main__':
    List=[]
    N=int(input('Enter number:'))
    for i in range(1,N+1):
        temp=fib(i)
        List.append(temp)
    for i in List:
        print(i),
    print('\n')
