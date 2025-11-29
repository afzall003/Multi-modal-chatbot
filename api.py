# api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from model_utils import handle_text_query, handle_image_query

app = Flask(__name__)
CORS(app)  # allows Streamlit (another port) to call this API

@app.route("/query/text", methods=["POST"])
def query_text():
    data = request.get_json() or {}
    question = data.get("question", "")
    answer = handle_text_query(question)
    return jsonify({"answer": answer})


@app.route("/query/image", methods=["POST"])
def query_image():
    if "image" not in request.files:
        return jsonify({"error": "No image file uploaded with key 'image'."}), 400

    image_file = request.files["image"]
    question = request.form.get("question", "")
    answer = handle_image_query(image_file, question)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    # debug=True auto-reloads on code changes
    app.run(host="0.0.0.0", port=5000, debug=True)
