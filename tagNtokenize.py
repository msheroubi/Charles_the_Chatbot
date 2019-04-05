import nltk
import pickle
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize
from os.path import dirname, join
from collections import Counter
import re
import spell

if __name__ == '__main__':
	train_text = state_union.raw("2005-GWBush.txt")
	custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
	with open('sent_tokenizer.pickle', 'wb') as f:
		pickle.dump(custom_sent_tokenizer, f)

#--------------------------------------------------------------------------------------

def tagNtokenize(strInput, isInput=False):
	current_dir = dirname(__file__)
	file_path = join(current_dir, 'sent_tokenizer.pickle')
	with open(file_path, 'rb') as f:
		custom_sent_tokenizer = pickle.load(f)

	file_path = join(current_dir, 'root_dict.pickle')
	with open(file_path, 'rb') as f:
		root_dict = pickle.load(f)


	tokenized = custom_sent_tokenizer.tokenize(strInput)
	tagged = []
	try:
		for t in tokenized:
			if(isInput and "PERSON" not in NER([(t, "NN")])):
				t = spell.correction(t)

			words2 = nltk.word_tokenize(t)

			for i in range(0, len(words2)-1):
				if(words2[i] in root_dict):
					words2[i] = root_dict[words2[i]]
			tagged = nltk.pos_tag(words2)
	except Exception as e:
		print(str(e))

	return tagged

def NER(tagged):
	return nltk.ne_chunk(tagged)
