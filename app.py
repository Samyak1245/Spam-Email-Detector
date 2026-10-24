import os
import joblib
from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

# Loaded at module level, so gunicorn loads them on import
model = joblib.load(os.path.join(BASE_DIR, "model", "spam_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "model", "vectorizer.pkl"))


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()[:5000]
        if message:
            vec = vectorizer.transform([message])
            pred = model.predict(vec)[0]
            idx = list(model.classes_).index(pred)
            confidence = round(float(model.predict_proba(vec)[0][idx]) * 100, 1)
            result = "SPAM" if pred == 1 else "NOT SPAM"

    return render_template(
        "index.html", result=result, confidence=confidence, message=message
    )


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__
