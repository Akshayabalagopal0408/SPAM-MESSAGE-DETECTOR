from flask import Flask, render_template, request
import pickle
import pandas as pd
from automata_filter import automata_detect

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        message = request.form['message']

        # Step 1: Automata check
        if automata_detect(message):
            result = "Spam (Automata)"
        else:
            # Step 2: AI check
            message_vec = vectorizer.transform([message])
            pred = model.predict(message_vec)[0]
            result = "Spam (AI Model)" if pred == "spam" else "Genuine"

        return render_template('result.html', message=message, result=result)
    return render_template('detect.html')

if __name__ == '__main__':
    app.run(debug=True)
