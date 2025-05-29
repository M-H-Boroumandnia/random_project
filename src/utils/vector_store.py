# src/utils/vector_store.py

import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("chat_history")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed(self, text: str):
        return self.model.encode(text).tolist()

    def add(self, chat_id: str, role: str, text: str):
        embedding = self.embed(text)
        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[f"{chat_id}-{role}-{hash(text)}"],
            metadatas=[{"chat_id": chat_id, "role": role}]
        )

    def search_similar(self, query: str, top_k: int = 3):
        embedding = self.embed(query)
        return self.collection.query(query_embeddings=[embedding], n_results=top_k)
