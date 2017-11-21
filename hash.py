
L=[1, 2, 3, 4, 5, 6,]

def hashFunction(n, N):
    return n%N


for i in range(0, 6):
    print ('L[{}] = {}'.format(i, L[i]))

print("the array must be cleared first")
L.clear()

print('Now the array is:')
print(L)
N=int(input('Enter your desired size:'))
print('Your entered values will be stored in the list using hashing')
print('Enter values:')
for i in range(0, N):
    num=int(input())
    index=hashFunction(num, N)
    L.insert(index, num)
print('Printing the values :')
for i in range(0, N):
    print ('L[{}] = {}'.format(i, L[i]))
