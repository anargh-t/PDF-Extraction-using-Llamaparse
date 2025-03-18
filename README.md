# PDF-Extraction-using-Llamaparse

## Overview
A web-based application that extracts text, tables, and images from PDFs.

## Features
- Extracts text from digital PDFs
- Identifies tables and converts them to LaTeX format
- Supports OCR for scanned PDFs

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/anargh-t/PDF_Extractor.git
   cd PDF_Extractor
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```sh
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## Project Structure
```
pdf_extractor/
├── static/
│   ├── css/
│   │   ├── styles.css
├── templates/
│   ├── index.html
│   ├── results.html
├── uploads/   # Uploaded PDFs
├── extracted/ # Extracted output (text, tables)
├── app.py
├── pdf_processing.py
├── table_extraction.py
├── text_extraction.py
├── requirements.txt
├── README.md
```

## Dependencies
- Flask
- llamaparse
- pdf2image
- pandas

## License
MIT License

