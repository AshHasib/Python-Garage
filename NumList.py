if __name__=='__main__':
    Numbers=[]
    total=0
    N=int(input("Enter the number of elements:"))
    for i in range(0,N):
        num=int(input("Enter element no {0} = ".format(i+1)))
        Numbers.append(num)
        total+=num
    print("The values are:"),
    for i in Numbers:
        print(i),
    print('\n')
    print('The total is = %d')%(total)