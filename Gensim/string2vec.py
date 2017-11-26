from gensim import corpora
documents= ["Human machine interface for lab abc computer applications",
                    "A survey of user opinion of computer system response time",
                    "The EPS user interface management system",
                    "System and human system engineering testing of EPS",
                    "Relation of user perceived response time to error measurement",
                    "The generation of random binary unordered trees",
                    "The intersection graph of paths in trees",
                    "Graph minors IV Widths of trees and well quasi ordering",
                    "Graph minors A survey"]
                
#This part will remove the common words and tokenize the sentences into words
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
            for document in documents]


from collections import defaultdict

frequency = defaultdict(int)
#This part will remove words that appear only once

for text in texts:
    for token in text:
        frequency[token] += 1
#This part stores the words in res which appeared more than once in the texts
texts = [[token for token in text if frequency[token] > 1]
for text in texts]

from pprint import pprint  # pretty-printer
pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict')
print(dictionary)
print(dictionary.token2id)


new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)
print(corpus)

class MyCorpus(object):
    def __iter__(self):
        for line in open('mySample.txt'):
# assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

corpus_memory_friendly = MyCorpus()  # doesn't load the corpus into memory!

print(corpus_memory_friendly)

for vector in corpus_memory_friendly:  # load one vector into memory at a time
    print(vector)
