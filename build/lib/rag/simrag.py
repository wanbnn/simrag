import numpy as np
import re
from collections import Counter

class SimpleRAG:
    def __init__(self):
        self.documents = []
        self.vocab = set()
        self.index = []
    
    def tokenize(self, text):
        """Tokeniza o texto removendo pontuações e transformando em minúsculas."""
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
        return text.split()
    
    def build_vocab(self, texts):
        """Cria um vocabulário baseado nos textos fornecidos."""
        for text in texts:
            tokens = self.tokenize(text)
            self.vocab.update(tokens)
    
    def text_to_vector(self, text):
        """Converte um texto em um vetor de frequência de palavras."""
        tokens = self.tokenize(text)
        word_count = Counter(tokens)
        return np.array([word_count.get(word, 0) for word in self.vocab], dtype=float)
    
    def add_documents(self, texts):
        """Adiciona documentos ao banco de dados e os vetorizados."""
        self.build_vocab(texts)
        self.documents.extend(texts)
        self.index = [self.text_to_vector(text) for text in self.documents]
    
    def cosine_similarity(self, vec1, vec2):
        """Calcula a similaridade do cosseno entre dois vetores."""
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        return np.dot(vec1, vec2) / (norm1 * norm2) if norm1 and norm2 else 0
    
    def search(self, query, top_k=3):
        """Busca os documentos mais relevantes baseados na similaridade do cosseno."""
        query_vector = self.text_to_vector(query)
        scores = [self.cosine_similarity(query_vector, doc_vector) for doc_vector in self.index]
        ranked_indices = np.argsort(scores)[::-1][:top_k]
        return [(self.documents[i], scores[i]) for i in ranked_indices]