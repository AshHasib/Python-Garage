

documents= open('Test.txt','r').readlines()


stoplist = set('for a of the and to in is our you or but from'.split())

texts = [[word for word in document.lower().split() if word not in stoplist]
		     for document in documents]
print(texts)

from collections import defaultdict
freq = defaultdict(int)

for text in texts:
	for token in text:
		freq[token]+=1
texts = [[token for token in text if freq[token]>1]
		for text in texts]
from pprint import pprint

pprint(texts)