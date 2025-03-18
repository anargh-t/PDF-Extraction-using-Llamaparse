from dotenv import load_dotenv
import os
from llama_cloud_services import LlamaParse
from llama_index.core import SimpleDirectoryReader
import pandas as pd

load_dotenv()


def extract_text_tables(pdf_path):
    """
    Uses Llama Cloud to extract text and tables from a PDF.

    :param pdf_path: Path to the PDF file
    :return: Extracted text and tables (as Pandas DataFrames)
    """
    parser = LlamaParse(result_type="markdown")
    file_extractor = {".pdf": parser}

    documents = SimpleDirectoryReader(input_files=[pdf_path], file_extractor=file_extractor).load_data()
    extracted_text = documents[0].text if documents else ""

    # Placeholder: Convert markdown tables into DataFrames (if needed)
    tables = []  # You can add logic to extract tables if Llama Cloud supports it.

    return extracted_text, tables
