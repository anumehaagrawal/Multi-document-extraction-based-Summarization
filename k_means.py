from sentence_array import sentence_array_final
import sentance_imp1 as fv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
import collections
def document_generate():
    doc_array = fv.get_documents()
    documents = []
    for doc in range(10):
        sentences = doc_array[doc][0].split(".")
        for group in sentences:
            documents.append(group)
    return documents

def k_means():
    documents = document_generate()
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents)
    transformer = TfidfTransformer(smooth_idf=False)
    tfidf = transformer.fit_transform(X)
    num_clusters = 8
    km = KMeans(n_clusters=num_clusters, random_state = 42)
    km.fit(tfidf)
    clustering = collections.defaultdict(list)
    for idx, label in enumerate(km.labels_):
        clustering[label].append(idx)

    summary = []
    for cl in range(len(clustering)):
        summary.append(documents[clustering[cl][0]])
    print(summary)

k_means()