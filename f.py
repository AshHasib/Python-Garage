'''def f(st):
    for i in st:
        if i != 'a' and i != 'A':
            return False
    return True '''
#f=lambda st: False not in[char in 'Aa' for char in st]
f=lambda st: all([char in 'Aa' for char in st])
print(f('AsdAaaa'))