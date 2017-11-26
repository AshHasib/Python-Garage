
def factorial(N):
    fact=1;
    for i in range(1,N+1):
        fact*=i
    return fact

x=int(input('Enter a number:'))
res=factorial(x)
print('{0} ! = {1}'.format(x,res))
