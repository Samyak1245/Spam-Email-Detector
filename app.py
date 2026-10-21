import os
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'spam_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'model', 'vectorizer.pkl')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

spam_class_idx = list(model.classes_).index(1) if hasattr(model, 'classes_') else 1

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    confidence = None
    status_class = None
    message = ""

    if request.method == 'POST':
        message = request.form.get('message', '').strip()

        if not message:
            return render_template(
                'index.html',
                result="Please provide email text to analyze.",
                status_class="warning",
                confidence=None,
                message=""
            )

        vec = vectorizer.transform([message])
        probs = model.predict_proba(vec)[0]
        spam_prob = probs[spam_class_idx]

        threshold = 0.50
        if spam_prob >= threshold:
            result = "Spam"
            confidence = round(spam_prob * 100, 2)
            status_class = "danger"   # Red flag
        else:
            result = "Not Spam"
            confidence = round((1 - spam_prob) * 100, 2)
            status_class = "success"  # Green flag

    return render_template(
        'index.html',
        result=result,
        confidence=confidence,
        status_class=status_class,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)
