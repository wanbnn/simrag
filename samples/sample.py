from rag.simrag import SimpleRAG

rag = SimpleRAG()
corpus = [
    "O céu está azul e o dia está lindo.",
    "Estou aprendendo sobre inteligência artificial.",
    "Python é uma linguagem poderosa para análise de dados."
]
rag.add_documents(corpus)
results = rag.search("Qual linguagem usar para análise de dados?")
for doc, score in results:
    print(f"Score: {score:.4f} - {doc}")