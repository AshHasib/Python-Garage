#from gensim import corpora

myDocs=['The definite article is the word the', 
                'It limits the meaning of a noun to one particular thing', 
                'The definite article tells you that your friend is referring to a specific party that both of you know about']


sList = set('the and to for but it that to with '.split())

text = [[word for word in doc.lower().split() if word not in sList] for doc in myDocs ]

for i in text:
    print(i)
