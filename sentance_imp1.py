import glob
import os 
import re
import string
import math

# Cleaning words to remove unnecessary punctuations
def cleaned_words(sentance):
	words = re.split(r'\W+', sentance)
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in words]
	final_words = []
	for word in stripped:
		if(word is not ''):
			final_words.append(word.lower())
	return final_words

# Creating frequency of words for a sentance and all sentances from a document are passed through this function
def create_frequency_dict(words,words_dict):	
	for word in words:
		word = word.lower()
		if word in words_dict:
			words_dict[word] = words_dict[word] + 1
		else:
			words_dict[word] = 1
	
#Calculate tf of all words in a document
def get_tf_docs(document):
	words_dict = dict()
	total_words_in_doc = 0
	sentances = document[0].split(".")
	tf_of_words = dict()

	for sentance in sentances:
		words_in_sentance = cleaned_words(sentance)
		total_words_in_doc = total_words_in_doc + len(words_in_sentance)
		create_frequency_dict(words_in_sentance,words_dict)

	for key,value in words_dict.items():
		tf_of_words[key] = value/total_words_in_doc

	return tf_of_words

#Calculate tf of all words in all documents so we know which word exists in which doc and what its importance is
def calculate_tf_all_docs(doc_order):
	dir = '/home/anumeha/Documents/Multi-document-extraction-based-Summarization/Cluster_of_Docs/d30001t'
	tf_of_words_in_all_docs = []
	for doc in os.listdir(dir):
		doc_order.append(int(doc[1:]))
		f=open(os.path.join( dir, doc ) ,"r") 
		sentances_dir = []
		for line in f:
			sentances_dir.append(line)
		get_tf_of_words_in_doc = get_tf_docs(sentances_dir)
		tf_of_words_in_all_docs.append(get_tf_of_words_in_doc)
	return tf_of_words_in_all_docs

#Calculate tf-idf of words in a sentance and then sum them up 
def tf_idf_sentance(sentance,doc_no):
	doc_nums = []
	tf_allwords = calculate_tf_all_docs(doc_nums)
	doc_no = doc_nums.index(doc_no)
	print(doc_no)
	words_of_sentance = cleaned_words(sentance)
	tf_idf_sum = 0
	for word in words_of_sentance:
		word = word.lower()
		tf_word = tf_allwords[doc_no][word]
		doc_count = 0
		for doc in tf_allwords:
			if word in doc.keys():
				doc_count = doc_count + 1
		idf_word = math.log(len(tf_allwords)/doc_count)
		tf_idf_sum = tf_idf_sum + (tf_word*idf_word)

	print(tf_idf_sum)
	return tf_idf_sum

tf_idf_sentance("Cambodia's two-party opposition asked the Asian Development Bank Monday to stop providing loans to the incumbent government, which it calls illegal.",1)