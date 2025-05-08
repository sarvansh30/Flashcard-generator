def retrieve_relevant_chunks(vectordb, query, k=3):
    docs = vectordb.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])
