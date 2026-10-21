import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model", "spam_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "model", "vectorizer.pkl"))


def classify(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    confidence = model.predict_proba(vec)[0][pred] * 100
    label = "SPAM" if pred == 1 else "NOT SPAM"
    return label, confidence


if __name__ == "__main__":
    samples = [
        "Congratulations! You won a free iPhone. Click here to claim now!",
        "Hey, are we still meeting for lunch tomorrow?",
        "URGENT: Your bank account is locked. Verify your details immediately.",
        "Can you send me the notes from today's lecture?",
    ]

    for msg in samples:
        label, conf = classify(msg)
        print(f"Message : {msg}")
        print(f"Result  : {label} ({conf:.1f}% confident)\n")
