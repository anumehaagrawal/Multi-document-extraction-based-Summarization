import sentance_imp1 as fv
		
maxLen = 100
decoder_stacks = [None for i in range(maxLen)]
sentences_array=[]

def create_sentence_val():
    doc_array = fv.get_documents()
    doc_order = fv.get_doc_order()
    print(doc_order)
    
    for doc in range(10):
        if(doc<len(doc_array) and len(doc_array[doc])>= 1):

            sentences = doc_array[doc][0].split(".")
            #doc_num = doc_order[doc]
            for group in sentences:
                print(group)
                feature_vec = fv.tf_idf_sentence(group,doc)
                mapping = [group,sum(feature_vec)]
                sentences_array.append(mapping)

def stack_decoder():
    for num in range(maxLen):
        for j in range(num):
            decoder_stacks[num].append(0)

create_sentence_val()
print(sentences_array)