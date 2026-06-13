import joblib

model = joblib.load('model/spam_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')


def predict_message(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]
    label = "Spam" if pred == 1 else "Not Spam"
    return label, max(prob)


if __name__ == "__main__":
    samples = [
        "Congratulations! You won a free lottery ticket, claim now by clicking this link",
        "Hey, are we still meeting at 5pm today?",
        "URGENT! Your account has been suspended. Verify immediately to avoid penalty.",
        "Can you send me the notes from today's class?"
    ]

    for msg in samples:
        label, confidence = predict_message(msg)
        print(f"Message: {msg}\nPrediction: {label} (confidence: {confidence:.2f})\n")
