# SimRag - Biblioteca de Recuperação Inteligente de Documentos

## Visão Geral
SimRag (“Simple Retrieval-Augmented Generation”) é uma biblioteca leve e eficiente para busca e recuperação de documentos utilizando similaridade do cosseno. Seu objetivo é permitir que você armazene, processe e recupere informações textuais de maneira rápida e intuitiva.

## Recursos Principais
- **Tokenização Inteligente**: Limpeza e processamento eficiente de textos.
- **Vocabulário Dinâmico**: Expande automaticamente conforme novos documentos são adicionados.
- **Representação Vetorial**: Converte textos em vetores numéricos para comparação.
- **Similaridade do Cosseno**: Identifica documentos mais relevantes para consultas.
- **Fácil Integração**: Projetado para ser simples e direto ao uso.

## Instalação
Como SimRag é uma biblioteca independente, basta copiar o arquivo `simrag.py` para seu projeto e importar conforme necessário.

## Guia de Uso
### Importação e Inicialização
```python
from rag.simrag import SimpleRAG
rag = SimpleRAG()
```

### Adicionando Documentos
```python
corpus = [
    "O céu está azul e o dia está lindo.",
    "Estou aprendendo sobre inteligência artificial.",
    "Python é uma linguagem poderosa para análise de dados."
]
rag.add_documents(corpus)
```

### Realizando uma Busca
```python
results = rag.search("Qual linguagem usar para análise de dados?")
for doc, score in results:
    print(f"Score: {score:.4f} - {doc}")
```

## Entendendo o Funcionamento
SimRag segue uma abordagem baseada em vetores para comparar documentos e consultas:
1. **Tokenização**: O texto é limpo e transformado em um conjunto de palavras-chave.
2. **Criação de Vetores**: Cada documento é convertido em um vetor de frequência de palavras.
3. **Similaridade do Cosseno**: A consulta do usuário também é vetorizada e comparada com os documentos armazenados.
4. **Rankeamento**: Os documentos mais similares à consulta são retornados ordenados por relevância.

## API da Biblioteca
Abaixo estão os principais métodos disponíveis:

### `tokenize(text: str) -> list`
Realiza a tokenização do texto, removendo pontuação e convertendo tudo para minúsculas.

### `build_vocab(texts: list) -> None`
Expande o vocabulário interno com palavras dos documentos fornecidos.

### `text_to_vector(text: str) -> np.array`
Converte um texto em um vetor baseado na frequência das palavras.

### `add_documents(texts: list) -> None`
Armazena novos documentos e atualiza o vocabulário.

### `cosine_similarity(vec1: np.array, vec2: np.array) -> float`
Calcula a similaridade do cosseno entre dois vetores.

### `search(query: str, top_k: int = 3) -> list`
Realiza uma busca e retorna os documentos mais relevantes.

## Casos de Uso
- **Chatbots**: Recupera informações rapidamente para respostas automatizadas.
- **Pesquisa em Documentos**: Facilita buscas em bases de conhecimento.
- **Análise de Texto**: Apoia classificação e clustering de textos.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para criar um fork e submeter um pull request.

## Licença
Este projeto está licenciado sob a MIT License.