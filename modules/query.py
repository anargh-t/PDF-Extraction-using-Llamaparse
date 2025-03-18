from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv

load_dotenv()


def query_document(documents, question):
    """
    Queries the indexed document using LlamaIndex and OpenAI.

    :param documents: Parsed documents from Llama Cloud
    :param question: User's query
    :return: AI-generated response
    """
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(question)

    return str(response)
