# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import io
import codecs
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd
from matplotlib import animation

class FileToSent(object):
    def __init__(self,filename):
        self.filename=filename
    def __iter__(self):
        for line in open(self.filename,'r', encoding='utf-8'):
            lines = [x for x in line.split()]
            yield lines
print("Enter the last file number :")
p=int(input())
for n in range(0,p):
    sentences = FileToSent('E:\Workspace\output%s.txt'% n )
    model = gensim.models.Word2Vec(sentences=sentences,window=4,min_count=1,workers=4,hs=1,size=10000)

print ("Enter a word : ")
x=input()

plt.rc('font', **{'sans-serif' : 'SolaimanLipi', 'family' : 'sans-serif'})
print (repr(model.most_similar(x)))
with io.open('E:\Workspace\output%s.txt'% n,'w',encoding='utf8') as f:
    f.write(repr(model.most_similar(x)))

vocab = list(model.wv.vocab)
x=model[vocab]

tsne = TSNE(n_components=2)
x_tsne = tsne.fit_transform(x)
df=pd.concat([pd.DataFrame(x_tsne),pd.Series(vocab)],axis=1)
df.columns=['x','y','word']
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(df['x'],df['y'],color=('red','green','blue','black'))
ax.set_title("Data Visualisation")
color_map={0:'red',1:'green'}
for i, txt in enumerate(df['word']):

    ax.annotate(txt,(df['x'].iloc[i],df['y'].iloc[i]))
plt.show()
