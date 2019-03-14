def document_generate():
    doc_array = fv.get_documents()
    documents = []
    for doc in range(10):
        sentences = doc_array[doc][0].split(".")
        for group in sentences:
            documents.append(group)
    print(documents)
    return documents


def extract_word_vec():
        # Extract word vectors from glove embedding
        word_embeddings = {}
        emb = open('glove.6B.100d.txt', encoding='utf-8')
        for line in emb:
                word_values = line.split()
                word = word_values[0]
                coefs = np.asarray(values[1:], dtype='float32')
                word_embeddings[word] = coefs
        emb.close()
        return word_embeddings

def page_rank():
        sentences = document_generate()