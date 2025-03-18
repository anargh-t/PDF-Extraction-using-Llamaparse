from flask import Flask, render_template, request, send_file
import os
from modules.extract import extract_text_tables
from modules.query import query_document
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf" not in request.files:
            return "No file part"

        pdf = request.files["pdf"]

        if pdf.filename == "":
            return "No selected file"

        if pdf and allowed_file(pdf.filename):
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
            pdf.save(file_path)

            text, tables = extract_text_tables(file_path)
            return render_template("result.html", text=text, tables=tables, filename=pdf.filename)

    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():
    question = request.form.get("query")
    pdf_file = request.form.get("pdf_file")
    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf_file)

    text, _ = extract_text_tables(pdf_path)
    response = query_document([text], question)

    return render_template("query.html", question=question, response=response)


@app.route("/download/<filename>")
def download_file(filename):
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
