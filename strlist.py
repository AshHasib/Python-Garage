if __name__=='__main__':
    Cars=["Toyota","Mercedes","Lambo",
        "Maruti","Vox","Ferrari","Rolls","Lambo","Toyota"]
    print(len(Cars)) #returns length
    print(Cars.count("Lambo")) #returns number of Lambo (2)
    print(Cars.index("Mercedes")) #returns 1, index number of Mercedes
    print(Cars.index("Lambo",4))# finds next Lambo string starting at position 4
    Cars.reverse()# Reverses the list
    for i in Cars:# printing the list
        print(i),
    print('\n')
    Cars.append("Corolla") #adds a new element at the end of the list
    for i in Cars:
        print(i),
    print('\n')
    Cars.sort()# sorts the list,in this case,alphabetically
    for i in Cars:
        print(i),
    print('\n')

    Cars.append("Ashok")
    print(Cars[len(Cars)-1])
    print(Cars[8])
    print((len(Cars)))
    #Cars.pop()
    Cars.pop(5)
    for i in Cars:
        print(i),
    print('\n')