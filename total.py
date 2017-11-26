if __name__=='__main__':
    total=0
    N=int(input("Enter how many elements:"))
    for i in range (0,N):
        num=int(input("Enter element no {0} = ".format(i+1)))
        total+=num
    print("The total is %d")%(total)