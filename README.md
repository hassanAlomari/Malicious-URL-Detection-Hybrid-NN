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

### Branch 1 — Character-Level Deep Sequence Encoder

The first branch is responsible for learning discriminative representations directly from raw URL character sequences. It combines convolutional feature extraction with bidirectional recurrent context modeling to capture both local malicious patterns and long-range dependencies.

```text
URL Character Sequence
        │
        ▼
Embedding Layer
(VOCAB_SIZE → EMBEDDING_DIM)
        │
        ▼
Conv1D (128 Filters, Kernel=3)
        │
Batch Normalization
        │
ReLU Activation
        │
        ▼
Conv1D (128 Filters, Kernel=4)
        │
Batch Normalization
        │
ReLU Activation
        │
        ▼
MaxPooling1D
        │
Dropout (0.30)
        │
        ▼
Bidirectional GRU (128 Units)
        │
        ▼
Learned URL Sequence Representation
```

#### Purpose of this Branch

* **Embedding Layer** transforms URL characters into dense vector representations.
* **Convolutional Layers** detect suspicious local patterns frequently observed in phishing and malicious URLs.
* **Batch Normalization** stabilizes training and accelerates convergence.
* **MaxPooling** reduces dimensionality while preserving dominant features.
* **Dropout** improves generalization and reduces overfitting.
* **Bidirectional GRU** captures sequential context from both directions, enabling the model to understand structural relationships across the entire URL.

This branch produces a high-level semantic representation of the URL's character sequence before fusion with handcrafted lexical features.

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

### Feature Fusion & Classification Head

To leverage both learned deep representations and handcrafted cybersecurity features, the outputs from the sequence encoder and the lexical feature encoder are fused through a feature concatenation layer.

```text
      Sequence Encoder Output
                 │
                 ▼
          ┌─────────────┐
          │             │
          ▼             ▼
        Concatenation Layer
                │
                ▼
        Dense (256) + ReLU
        Batch Normalization
          Dropout (0.40)
                │
                ▼
        Dense (128) + ReLU
          Dropout (0.30)
                │
                ▼
        Sigmoid Output Layer
                │
                ▼
        Malicious Probability Score
```

The classification head applies regularized fully connected layers with L2 regularization, batch normalization, and dropout to improve robustness and generalization while producing a calibrated maliciousness probability score.

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
