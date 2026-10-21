import os
import joblib
from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

model = joblib.load(os.path.join(BASE_DIR, "model", "spam_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "model", "vectorizer.pkl"))


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    confidence = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if message:
            vec = vectorizer.transform([message])
            pred = model.predict(vec)[0]
            confidence = round(model.predict_proba(vec)[0][pred] * 100, 1)
            result = "SPAM" if pred == 1 else "NOT SPAM"

    return render_template("index.html", result=result, confidence=confidence, message=message)


if __name__ == "__main__":
    app.run(debug=True)
