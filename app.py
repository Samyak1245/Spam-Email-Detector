from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('model/spam_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    confidence = None
    message = ""

    if request.method == 'POST':
        message = request.form['message']
        vec = vectorizer.transform([message])
        pred = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]
        result = "Spam" if pred == 1 else "Not Spam"
        confidence = round(max(prob) * 100, 2)

    return render_template('index.html', result=result, confidence=confidence, message=message)


if __name__ == '__main__':
    app.run(debug=True)
