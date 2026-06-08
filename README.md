# 🛡️ Malicious URL Detection System

### Hybrid Deep Learning Pipeline for Real-Time Phishing and Malicious URL Detection

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 Project Overview

Malicious URLs remain one of the most common attack vectors used in phishing campaigns, malware distribution, and credential theft.

This project presents a complete end-to-end AI-powered detection system capable of classifying URLs as **Benign** or **Malicious** in real time.

Unlike traditional blacklist-based approaches, the system leverages a **Hybrid Deep Learning Architecture (CNN + BiGRU + Dense Features Network)** that learns both:

* Character-level URL patterns
* Sequential URL structures
* Handcrafted lexical and statistical features

The solution is deployed as a production-ready application using:

* FastAPI for serving predictions
* Streamlit for user interaction
* TensorFlow/Keras for deep learning inference

---

## 🎯 Key Features

✅ Real-time malicious URL classification

✅ Hybrid Neural Network Architecture

✅ Character-level URL representation

✅ Manual lexical feature extraction

✅ FastAPI REST API deployment

✅ Interactive Streamlit dashboard

✅ Domain-aware train/validation/test splitting

✅ Confidence score estimation

✅ Production-ready inference pipeline

---

## 🏛️ System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
URL Preprocessor
 │
 ├── Character Tokenization
 └── Lexical Feature Extraction
 │
 ▼
Hybrid Neural Network
(CNN + BiGRU + Dense)
 │
 ▼
Prediction + Confidence Score
 │
 ▼
JSON Response
```

---

## 🧠 Deep Learning Model

### Hybrid Architecture

The model combines two complementary learning branches:

### Branch 1 — Character Sequence Learning

```text
Input URL
    ↓
Embedding Layer
    ↓
Conv1D
    ↓
BiGRU
```

This branch captures:

* Suspicious character patterns
* Obfuscation techniques
* Sequential URL relationships

### Branch 2 — Lexical Feature Learning

Examples of extracted features:

* URL Length
* Domain Length
* Path Length
* Entropy
* Digit Count
* Special Character Count
* IP Address Usage
* HTTPS Usage
* Subdomain Count
* Suspicious Token Indicators

```text
Numerical Features
      ↓
Dense Layers
```

### Fusion Layer

Both branches are concatenated and passed through fully connected layers to generate the final threat probability.

---

## 📂 Repository Structure

```text
.
├── build_classifier.ipynb
├── preprocess_url.py
├── main.py
├── UI.py
├── scaler (2).pickle
├── best_url_model (2)_final.keras
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Layer           | Technology         |
| --------------- | ------------------ |
| Deep Learning   | TensorFlow / Keras |
| API             | FastAPI            |
| Frontend        | Streamlit          |
| ML Utilities    | Scikit-Learn       |
| Data Processing | Pandas, NumPy      |
| Deployment      | Uvicorn            |

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/hassanAlomari/Malicious-URL-Detection-Hybrid-NN.git

cd Malicious-URL-Detection-Hybrid-NN
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Interactive API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 💻 Running the Frontend

```bash
streamlit run UI.py
```

---

## 🔌 API Example

### Request

```json
{
  "url": "http://example-malicious-site.com"
}
```

### Response

```json
{
  "url": "http://example-malicious-site.com",
  "label": "Malicious",
  "confidence": 0.9845
}
```

---

## 📊 Model Performance

Add your final metrics here:

| Metric    | Score |
| --------- | ----- |
| Accuracy  | XX%   |
| Precision | XX%   |
| Recall    | XX%   |
| F1 Score  | XX%   |
| ROC-AUC   | XX%   |

---

## 📸 Application Preview

Add screenshots of:

* Streamlit Dashboard
* Prediction Results
* API Documentation

Example:

```markdown
![Dashboard](images/dashboard.png)
```

---

## 🔮 Future Improvements

* Transformer-based URL Encoder
* Explainable AI (XAI)
* Docker Deployment
* CI/CD Integration
* Online Learning Pipeline
* Threat Intelligence Integration

---

## 👨‍💻 Author

**Hassan Alomari**

AI & Machine Learning Engineer

GitHub:
https://github.com/hassanAlomari

---

## 📜 License

This project is released under the MIT License.
