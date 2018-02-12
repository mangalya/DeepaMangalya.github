
import json
from PyDictionary import PyDictionary
import nltk
from nltk.corpus import wordnet

myFile=open('sample.json', 'r')
myObject=myFile.read()

data = myObject.strip("\u00ef\u00bb\u00bf")

data_file = json.loads(data)
print(data_file)


# for key,value in data_file.items():
	
# 	for key,val in value.items():

# 		for i in range(len(val)):
# 		   get = val[i]

# 		   dictionary=PyDictionary(get)
# 		   sample= dictionary.getSynonyms()
# 		   print(sample)
# 		   w1 = wordnet.synset('get.v.01') 
# 		   w2 = wordnet.synset('sample.v.01')
# 		   print(w1.wup_similarity(w2))
		

		
			
	
