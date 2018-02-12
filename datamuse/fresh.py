import json
import datamuse
from datamuse import Datamuse


myFile = open("library.json", 'r')
myObject=myFile.read()
data=json.loads(myObject)

api = datamuse.Datamuse()
title=[]
d=[]
final=[]
for key,value in data.items():
	for k,val in value.items():
		
		for a in val:
			title.append(a)
			# print(a)
			wordlist = api.words(rel_syn=a, max=10)
			# print(a,wordlist)

			for dict in wordlist:
				b= dict['word']
				# print(b)
				d.append(b)
		final.append(d)
# print(title)
# print(final)
x={}
# 
l=len(title)
for i in range(0,l):
	x.update({title[i]:final[i]})
# print(x)









# similarity using wordnet

# for key,value in x.items():
# 	for val in value:
# 	    # print("val",val)
# 	    # print("synset of key")
# 	    wordFromlist1= wn.synsets(key)
# 	    # print(wordFromlist1)
# 	    # print("synset of val")
# 	    wordFromlist2 = wn.synsets(val)
# 	    # print(wordFromlist2)
# 	    # print("similarity:")
# 	    if wordFromlist1 and wordFromlist2:
# 	    	s=wordFromlist1[0].wup_similarity(wordFromlist2[0])
