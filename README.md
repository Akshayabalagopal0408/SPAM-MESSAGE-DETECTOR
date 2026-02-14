📩 Spam Message Detector (Automata + AI)

📌 Project Overview
This project detects whether a given message is Genuine or Fake/Spam using a hybrid approach that combines:
🔹 Automata-based pattern detection (Regex rules)
🔹 Machine Learning model (Naive Bayes classifier)

The system is implemented as a Flask web application with a simple 3-page interface:
Home → Input → Result

🛠️ Technologies Used
Python
Flask
scikit-learn
pandas
HTML
CSS

⚙️ Project Structure
SPAM-MESSAGE-DETECTOR/
│
├── app.py
├── ai_model.py
├── automata_filter.py
├── dataset/
│   └── messages.csv
├── templates/
├── static/
├── requirements.txt

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/SPAM-MESSAGE-DETECTOR.git
cd SPAM-MESSAGE-DETECTOR

2️⃣ Create a Virtual Environment
python -m venv venv

Activate it:

Git Bash
source venv/Scripts/activate

Windows CMD
venv\Scripts\activate

3️⃣ Install Required Dependencies
pip install -r requirements.txt

4️⃣ Train the AI Model
python ai_model.py

This will:
Train the Naive Bayes model
Generate model.pkl and vectorizer.pkl

5️⃣ Run the Flask Application
python app.py

6️⃣ Open in Browser
Go to:
http://127.0.0.1:5000

🔎 How It Works
The Automata Layer checks for suspicious keywords such as:
urgent
free
click
breaking
exclusive
The AI Layer classifies the message using a trained Naive Bayes model.
If either layer detects spam → the message is classified as Fake/Spam.

🚀 Future Improvements
Improve dataset size for better AI accuracy
Add confidence score display
Deploy to cloud (Render / Heroku)
Extend detection to fake news articles
