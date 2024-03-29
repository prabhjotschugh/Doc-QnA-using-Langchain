# Document QnA using Langchain

Document QnA using Langchain is a robust solution designed to enable question answering on textual documents, employing advanced natural language processing techniques. This project integrates OpenAI's embedding model for semantic understanding, FAISS library for efficient similarity searches, and Langchain's pre-trained question answering models.

# Features
- Embedding Generation: OpenAI's embedding model is utilized to generate numerical representations of words and phrases from textual data. These embeddings capture the semantic meaning of the text, facilitating accurate understanding of context.

- Search Index Creation: The solution organizes the generated embeddings into a search index using the FAISS library. This index structure enables rapid and efficient similarity searches, enhancing the retrieval of relevant information from the document.

- Question Answering Model: Langchain's pre-trained question answering models are seamlessly integrated into the solution. These models are adept at comprehending questions and extracting precise answers from the provided textual context.

- Query Execution: Users can input their questions into the system, which then executes queries against the search index using the loaded question answering model. This process matches the query with relevant embeddings in the index to retrieve context-aware answers promptly.

# Demo
https://github.com/prabhjotschugh/Doc-QnA-using-Langchain/assets/64200536/cdbd6493-3455-464b-ad12-82e1928fdf58
