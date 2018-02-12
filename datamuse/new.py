import datamuse
from datamuse import Datamuse
import json
import nltk
# from nltk.corpus import wordnet
# import itertools as IT

myFile=open('library.json', 'r')
myObject=myFile.read()
data = json.loads(myObject)


final=[]
title=[]

api = datamuse.Datamuse()

for key, value in data.items():
	for ke,val in value.items():
		for a in val:
			wordlist = api.words(rel_syn=a, max=10)
			test=[]
			test.append(a)
			title.append(a)
			for dict in wordlist:
				example= dict['word']
				test.append(example)
 			
			final.append(test)
# print(final)
# print(title)

x={}

l=len(title)
# print(l)
for i in range(0,l):
	x.update({title[i]:final[i]})
data['user empathy map']['think and feel']=x
f=open('library.json','w')
a=f.write(json.dumps(data))






