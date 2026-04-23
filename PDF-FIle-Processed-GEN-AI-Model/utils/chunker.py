def chunk_text(text, size=800, overlap=100):
    chunks=[]
    i=0
    while i < len(text):
        chunks.append(text[i:i+size])
        i += size-overlap
    return chunks
