# 🛡️ End-to-End Malicious URL Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B.svg)

## 📌 Overview
This repository hosts a complete, production-ready AI system designed to detect and classify URLs as **Benign** or **Malicious**. The project goes beyond model training by deploying the hybrid deep learning model via a robust **FastAPI** backend and an interactive **Streamlit** frontend. 

The underlying AI model utilizes a **Hybrid Neural Network (1D CNN + BiGRU + Dense)** to analyze spatial character patterns, sequential context, and handcrafted lexical features with high precision.

## 🏗️ System Architecture
The project is built using a modern microservice-like approach, separated into three core components:

1. **The Deep Learning Model (`build_classifier.ipynb`):**
   * Processes tokenized text sequences via Embedding, Conv1D, and Bidirectional GRU layers.
   * Processes 10 manual digital features (e.g., entropy, IP presence, path length) via a Dense network.
   * Concatenates outputs to provide a final threat probability score.
   * Uses **Domain-Aware Splitting** during training to prevent data leakage.

2. **The Backend API (`main.py`):**
   * Built with **FastAPI** for high performance and asynchronous request handling.
   * Uses FastAPI `lifespan` to load the pre-trained Keras model (`best_url_model (2)_final.keras`) and StandardScaler (`scaler (2).pickle`) into memory at startup.
   * Exposes a `POST /predict` endpoint that handles incoming URL requests, processes them using the custom `URLPreprocessor`, and returns a JSON response with the threat label and confidence score.

3. **The Frontend UI (`UI.py`):**
   * A clean, interactive **Streamlit** web application.
   * Takes user input, sends a POST request to the deployed FastAPI backend, and renders visual alerts based on the URL's safety status.

## 📂 Repository Structure

```text
├── .gitignore
├── requirements.txt
├── main.py                          # FastAPI backend application
├── UI.py                            # Streamlit frontend application
├── preprocess_url.py                # Custom URL feature extraction class
├── scaler (2).pickle                # Saved StandardScaler for numeric features
├── best_url_model (2)_final.keras   # Trained Hybrid Neural Network
└── build_classifier.ipynb           # Model training, evaluation, and EDA

🚀 Installation & Running Locally
1. Setup the Environment
Clone the repository and install all required full-stack dependencies:
git clone [https://github.com/hassanAlomari/Malicious-URL-Detection-Hybrid-NN.git](https://github.com/hassanAlomari/Malicious-URL-Detection-Hybrid-NN.git)
cd Malicious-URL-Detection-Hybrid-NN

# Install required packages
pip install fastapi uvicorn tensorflow scikit-learn pandas pydantic streamlit requests

2. Start the FastAPI Backend
Run the backend server to load the model and expose the API endpoint:
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000. You can view the interactive API documentation at http://127.0.0.1:8000/docs.

3. Start the Streamlit Frontend
In a new terminal window, run the user interface:
streamlit run UI.py
Make sure the endpoint URL in UI.py points to your local FastAPI server (e.g., http://127.0.0.1:8000/predict) during local testing.

🔌 API Reference
Endpoint: POST /predict

Request Body (JSON):
{
  "url": "[http://example-malicious-site.com](http://example-malicious-site.com)"
}

Response (JSON):
{
  "url": "[http://example-malicious-site.com](http://example-malicious-site.com)",
  "label": "Malicious 💀",
  "confidence": 0.9845
}




