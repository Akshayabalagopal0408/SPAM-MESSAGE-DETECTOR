# 📩 Spam Message Detector (Automata + AI)

## 📌 Project Overview
This project detects whether a given message is **Genuine** or **Fake/Spam** using a hybrid approach that combines:

- Automata-based pattern detection (Regex rules)
- Machine Learning model (Naive Bayes classifier)

---

## 🛠️ Tech Stack
- Python  
- Flask  
- scikit-learn  
- pandas  
- HTML  
- CSS  

---

## 📂 Project Structure

```
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
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/SPAM-MESSAGE-DETECTOR.git
cd SPAM-MESSAGE-DETECTOR
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
source venv/Scripts/activate
```

OR (Windows CMD)

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the AI Model

```bash
python ai_model.py
```

### 5️⃣ Run the Application

```bash
python app.py
```

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔎 How It Works

1. Automata layer checks for suspicious keywords.
2. AI model classifies message using trained data.
3. If either detects spam → Message is labeled Fake/Spam.

---

## 🚀 Future Improvements
- Improve dataset size  
- Add confidence score  
- Deploy to cloud  


