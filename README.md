# PDF Extraction & Querying with LlamaParse

## 📌 Project Overview
This Flask-based web application allows users to **upload PDFs**, **extract text and tables**, and **query the extracted content** using the **LlamaParse** library. The extracted data is displayed in a clean and organized manner with an intuitive UI.

---

## 🚀 Features
- **Upload PDF** files for extraction.
- **Extract Text & Tables** from PDFs using `LlamaParse`.
- **Display Extracted Data** in a structured format.
- **Query Extracted Content** using an LLM.
- **Download the Processed PDF**.
- **Responsive & Attractive UI** built with HTML, CSS, and Bootstrap.

---

## 📂 Project Structure
```
📦 pdf-extraction-flask
 ┣ 📂 static                # CSS, JavaScript, images
 ┃ ┣ 📜 styles.css          # Custom styles
 ┃ ┣ 📜 script.js           # JavaScript for interactivity (optional)
 ┣ 📂 templates             # HTML templates
 ┃ ┣ 📜 index.html          # Upload PDF page
 ┃ ┣ 📜 result.html         # Display extracted text & tables
 ┃ ┣ 📜 query.html          # Query extracted content
 ┣ 📂 uploads               # Stores uploaded PDFs
 ┣ 📂 modules               # PDF processing modules
 ┃ ┣ 📜 extract.py          # Extract text & tables
 ┃ ┣ 📜 query.py            # Query extracted text
 ┣ 📜 app.py                # Main Flask application
 ┣ 📜 config.py             # Configuration settings
 ┣ 📜 .env                  # API keys for Llama Cloud & OpenAI
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 README.md             # Documentation
 ┣ 📜 .gitignore            # Ignore unnecessary files
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anargh-t/PDF-Extraction-using-Llamaparse.git
cd PDF-Extraction-using-Llamaparse
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys
Create a `.env` file in the project root and add your **Llama Cloud API key**:
```env
LLAMA_CLOUD_API_KEY=llx-xxxxxx
OPENAI_API_KEY=sk-proj-xxxxxx
```

### 5️⃣ Run the Flask Application
```bash
python app.py
```

### 6️⃣ Open in Browser
```
http://127.0.0.1:5000/
```

---

## 📌 Usage
1️⃣ **Upload a PDF** on the homepage.
2️⃣ **Extracted Text & Tables** will be displayed.
3️⃣ **Query the extracted content** using a search bar.
4️⃣ **Download the PDF** if needed.

---

## 📜 Example Output
### **Extracted Text**
```
This is a sample extracted text from the uploaded PDF.
```

### **Extracted Tables**
| Column 1 | Column 2 |
|----------|----------|
| Data A   | Data B   |
| Data C   | Data D   |

---

## 🔧 Troubleshooting
### 🔹 Invalid API Key Error
- Ensure `.env` contains the **correct** `LLAMA_CLOUD_API_KEY`.
- Try **generating a new API key** from the Llama Cloud API dashboard.

### 🔹 Flask App Not Running
- Ensure dependencies are installed correctly: `pip install -r requirements.txt`.
- Check if the **correct Python version** is being used (`python --version`).

---

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push the branch and create a PR.

---

## 📜 License
This project is licensed under the MIT License.

---

## 📬 Contact
For issues and suggestions, create an **Issue** on GitHub or reach out at **your-email@example.com**.

