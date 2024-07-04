# Document QnA using Langchain 📚🔍

<b>Live Link</b> - https://prabhjotschugh-genai-doc-qna.onrender.com/

Document QnA using Langchain is a robust solution designed to enable question answering on textual documents, employing advanced natural language processing techniques. This project integrates OpenAI's embedding model for semantic understanding, FAISS library for efficient similarity searches, and Langchain's pre-trained question answering models.

## Features

- **Embedding Generation:** OpenAI's embedding model is utilized to generate numerical representations of words and phrases from textual data. These embeddings capture the semantic meaning of the text, facilitating accurate understanding of context.

- **Search Index Creation:** The solution organizes the generated embeddings into a search index using the FAISS library. This index structure enables rapid and efficient similarity searches, enhancing the retrieval of relevant information from the document.

- **Question Answering Model:** Langchain's pre-trained question answering models are seamlessly integrated into the solution. These models are adept at comprehending questions and extracting precise answers from the provided textual context.

- **Query Execution:** Users can input their questions into the system, which then executes queries against the search index using the loaded question answering model. This process matches the query with relevant embeddings in the index to retrieve context-aware answers promptly.

## Repository Structure

- `app-openai.py`: Contains the implementation of the question answering system using OpenAI's models.
- `app.py`: Implements the question answering system using open-source models.
- `index.html`: HTML template for the frontend interface.
- `styles.css`: CSS styles for the frontend interface.

## Usage

To run the application:
1. Clone the repository:
   ```bash
   git clone https://github.com/prabhjotschugh/Doc-QnA-using-Langchain
   cd document-qna-using-langchain
    ```

2. Install the required Python packages:
    ```sh
    pip install -r req.txt
    ```

3. Set your OpenAI API key (if using OpenAI's model):
    ```sh
    export OPENAI_API_KEY="your-openai-api-key"
    ```

4. Set your HuggingFace API key (if using open-source models):
    ```sh
    export HUGGINGFACEHUB_API_TOKEN="your-huggingface-api-key"
    ```


## Running the Flask App

1. Start the Flask app:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.



# Outputs 

![1](https://github.com/prabhjotschugh/Doc-QnA-using-Langchain/assets/64200536/170fedd0-7b4c-46bf-8dc9-ce2169d04920)

![2](https://github.com/prabhjotschugh/Doc-QnA-using-Langchain/assets/64200536/6a5afb0f-b467-404e-995b-2f3c75a7d2b6)


# Demo
https://github.com/prabhjotschugh/Doc-QnA-using-Langchain/assets/64200536/cdbd6493-3455-464b-ad12-82e1928fdf58

https://github.com/prabhjotschugh/Doc-QnA-using-Langchain/assets/64200536/f9125848-5264-4bbf-be54-81f7954c004b


