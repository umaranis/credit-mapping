from flask import Flask, jsonify, request
import PyPDF2
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-mpnet-base-v2')

app = Flask(__name__)

# API endpoint for sentence similarity
@app.route("/api/sentence-similarity", methods=["POST"])
def handle_sentence_similarity():
    sentence1 = request.form['sentence1']
    sentence2 = request.form['sentence2']
    similarity_result = compute_sentence_similarity(sentence1, sentence2)
    return jsonify({"sentence_similarity_result": similarity_result})

def compute_sentence_similarity(sentence1, sentence2):
    # Your existing similarity computation logic...
    return f"Similarity Score: {str(cosine_scores)[11:13]}%"

# Your existing functions...

if __name__ == "__main__":
    app.run(debug=True)