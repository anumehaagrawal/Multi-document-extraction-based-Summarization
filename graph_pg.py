def document_generate():
    doc_array = fv.get_documents()
    documents = []
    for doc in range(10):
        sentences = doc_array[doc][0].split(".")
        for group in sentences:
            documents.append(group)
    print(documents)
    return documents