from flask_cors import CORS
from flask import Flask, jsonify, request
import PyPDF2
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-mpnet-base-v2')

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# API endpoint for sentence similarity
@app.route("/api/sentence-similarity", methods=["POST"])
def handle_sentence_similarity():
    #sentence1 = request.form['sentence1']
    #sentence2 = request.form['sentence2']

    print(request.json)
    sentence1 = request.json.get('sentence1')
    sentence2 = request.json.get('sentence2')
    print(sentence1, sentence2)

    similarity_result = compute_sentence_similarity(sentence1, sentence2)
    return jsonify({"sentence_similarity_result": similarity_result})

def compute_sentence_similarity(sentence1, sentence2):
    cosine_scores = None
    cosine_score_strings = []
    
    embeddings1 = model.encode(sentence1, convert_to_tensor=True)
    embeddings2 = model.encode(sentence2, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    cosine_score_strings.append(cosine_scores)

    return f"Similarity Score: {str(cosine_scores)[11:13]}%"

# Your existing functions...

if __name__ == "__main__":
    app.run(debug=True)