# Spam Email Classifier

A machine learning project that classifies email/SMS messages as **Spam** or **Ham (Not Spam)** using **TF-IDF vectorization** and a **Multinomial Naive Bayes** classifier. Built as part of the AIML Summer Internship at Codec Technologies.

## Overview

Spam detection is a classic text classification problem. This project:
- Cleans and vectorizes message text using **TF-IDF**.
- Trains a **Multinomial Naive Bayes** classifier on the SMS Spam Collection dataset.
- Evaluates performance using accuracy, precision, recall, and F1-score.
- Provides a simple **Flask web app** for live predictions.

## Project Structure

```
spam-classifier/
│
├── data/
│   ├── README.md          # dataset download instructions
│   └── spam.csv            # dataset (download separately, see data/README.md)
│
├── model/
│   ├── spam_model.pkl       # trained Naive Bayes model (generated after training)
│   └── vectorizer.pkl       # fitted TF-IDF vectorizer (generated after training)
│
├── templates/
│   └── index.html           # frontend for the Flask app
│
├── train.py                 # script to train and evaluate the model
├── predict.py                # script to test predictions on sample messages
├── app.py                     # Flask app for interactive demo
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repo and install dependencies
```bash
git clone <your-repo-url>
cd spam-classifier
pip install -r requirements.txt
```

### 2. Add the dataset
Follow the instructions in `data/README.md` to download and place `spam.csv` in the `data/` folder.

### 3. Train the model
```bash
python train.py
```
This will print accuracy, classification report, and confusion matrix, and save the trained model + vectorizer to the `model/` folder.

### 4. Test predictions
```bash
python predict.py
```

### 5. Run the web app
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your browser, paste an email/message, and click **Classify**.

## Approach

| Step | Technique |
|------|-----------|
| Text Vectorization | TF-IDF (Term Frequency–Inverse Document Frequency) |
| Classifier | Multinomial Naive Bayes |
| Train/Test Split | 80/20, stratified |
| Evaluation Metrics | Accuracy, Precision, Recall, F1-score, Confusion Matrix |

## Results

After training, the model typically achieves **~96–98% accuracy** on the test set (varies slightly with random seed and dataset version).

## Why Naive Bayes for Spam Detection?

Naive Bayes assumes that features (words) are conditionally independent given the class label. While this is rarely true in real text (word order and co-occurrence matter), the algorithm still performs surprisingly well for spam filtering because the *presence* of certain words (e.g., "free", "winner", "urgent") is itself a strong, largely independent signal of spam — the independence assumption doesn't need to be perfectly true for the classifier to rank classes correctly.

## Future Improvements
- Try SVM or Logistic Regression and compare performance.
- Use n-grams (bigrams/trigrams) in TF-IDF for better context capture.
- Add lemmatization/stemming during preprocessing.
- Deploy the Flask app on a cloud platform (Render/Heroku).

