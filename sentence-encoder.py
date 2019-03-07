import sentance_imp1 as fv
from sklearn.metrics.pairwise import cosine_similarity

maxLen = 101
decoder_stacks = [[ ] for i in range(maxLen)]
sentences_array=[]

def cosine_similarity(sentences,sentence_vectors):
	sim_mat = np.zeros([len(sentences), len(sentences)])
	for i in range(len(sentences)):
		for j in range(len(sentences)):
			if i != j:
				sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]
	return sim_mat

def create_sentence_val():
    doc_array = fv.get_documents()
    doc_order = fv.get_doc_order()

    print(doc_order)
    
    for doc in range(10):
        if(doc<len(doc_array) and len(doc_array[doc])>= 1):

            sentences = doc_array[doc][0].split(".")
            #doc_num = doc_order[doc]
            for group in sentences:
                feature_vec = fv.tf_idf_sentence(group,doc)
                mapping = [group,sum(feature_vec)]
                sentences_array.append(mapping)

def importance(sentence_stack):
    sum =0
    for i in sentence_stack:
        sum+=sentance_stack[1]
    return sum

def stack_decoder():
    threshold=0.5
    stack=[] #priority queue
    for i in range(maxLen):
        for j in decoder_stacks:
            for s in sentences_array:
                newLen=maxLen+1
                #decoder_stacks[num].append(0)
                if i+ len(s)<maxLen:
                    newLen=i+len(s[0])
                    if len(j)==0:
                        j.append(s)
                    elif cosine_similarity(s[0],j[0]) < threshold:
                        j.append(s)
                    score=importance(j)
                    decoder_stacks[newLen].append([j,score])
    print(decoder_stacks)

                    
                    


create_sentence_val()
print(sentences_array)
