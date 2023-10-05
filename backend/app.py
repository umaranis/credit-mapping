from flask_cors import CORS
from flask import Flask, jsonify, request
import PyPDF2
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-mpnet-base-v2')

app = Flask(__name__)
#CORS(app, resources={r"/api/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})
CORS(app)

# API endpoint for sentence similarity
@app.route("/api/sentence-similarity", methods=["GET", "POST"])
def handle_sentence_similarity():
    #sentence1 = request.form['sentence1']
    #sentence2 = request.form['sentence2']

    print(request.json)
    sentence1 = request.json.get('sentence1')
    sentence2 = request.json.get('sentence2')
    print(sentence1, sentence2)

    similarity_result, similarity_score = compute_sentence_similarity(sentence1, sentence2)
    return jsonify({"sentence_similarity_result": similarity_result, "similarity_score": similarity_score})

def compute_sentence_similarity(sentence1, sentence2):
    cosine_scores = None
    cosine_score_strings = []
    
    embeddings1 = model.encode(sentence1, convert_to_tensor=True)
    embeddings2 = model.encode(sentence2, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    cosine_score_strings.append(cosine_scores)

    return f"Similarity Score: {str(cosine_scores)[11:13]}%", float(cosine_scores)

@app.route("/api/upload-pdf", methods=["POST"])
def upload_pdf():
    pdf_text1 = ""

    uploaded_file1 = request.files["file1"]

    if uploaded_file1.filename != "":
            if uploaded_file1.filename.endswith(".pdf"):
                pdf_text1 = extract_text_from_pdf(uploaded_file1)

                #return jsonify({"pdf_text": pdf_text1})
                return pdf_text1

    return jsonify({"error": "No PDF file uploaded"})
    
def extract_text_from_pdf(uploaded_file):
    pdf_text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
    except Exception as e:
        return f"Error extracting text: {str(e)}"
    return pdf_text

if __name__ == "__main__":
    app.run(debug=True)