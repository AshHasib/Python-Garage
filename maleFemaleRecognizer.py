from sklearn import tree

X=[[180, 40, 37],[181, 41, 38], [175, 36, 34], [182, 40, 38],
    [172, 38, 35], [176, 37, 36], [182, 40, 39], 
    [178, 38, 37], [185, 42, 38], [173, 33, 32], [188, 43, 40]]
    
Y=['male', 'male', 'female', 'male', 'female', 'female', 
    'male', 'female', 'male', 'female', 'male']

clf=tree.DecisionTreeClassifier()

clf=clf.fit(X, Y)
x=int(input('Enter height:'))
y=int(input('Enter chest bredth:'))
z=int(input('Enter face bredth:'))
prediction=clf.predict([[x, y, z]])

print (prediction)
