import faiss, numpy as np

def embed(text):
    vec=np.random.rand(384).astype('float32')
    return vec

def build_index(chunks):
    dim=384
    index=faiss.IndexFlatL2(dim)
    vectors=np.array([embed(c) for c in chunks]).astype('float32')
    index.add(vectors)
    return index

def search_index(index, chunks, query, k=3):
    q=np.array([embed(query)]).astype('float32')
    _,I=index.search(q,k)
    return [chunks[i] for i in I[0] if i < len(chunks)]
