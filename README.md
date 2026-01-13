🌐 Multilingual Translation System (JA → EN → HI)

A full-stack multilingual translation application that translates Japanese → English → Hindi using a machine learning model served via FastAPI and accessed through a Streamlit frontend.

English is used as an intermediate language to improve translation quality and maintain semantic accuracy.

🚀 Features

🇯🇵 Japanese → 🇬🇧 English → 🇮🇳 Hindi translation

⚡ FastAPI backend for model inference

🎨 Streamlit frontend for interactive usage

🔌 REST API support

🧠 Transformer-based NLP model

📦 Easy setup with requirements.txt

🔄 Scalable architecture for adding more languages

🏗️ Project Architecture
multilingual-translator/
│
├── backend/
│   ├── main.py              # FastAPI app
│   ├── model.py             # Translation model logic
│   └── requirements.txt     # Backend dependencies
│
├── frontend/
│   └── app.py               # Streamlit UI
│
├── README.md
└── .gitignore

🔄 Translation Pipeline
Japanese Text
     ↓
Japanese → English Model
     ↓
English → Hindi Model
     ↓
Hindi Output


English acts as an intermediate bridge to ensure higher translation accuracy.

🧠 Technologies Used
Backend

FastAPI – REST API framework

Transformers (Hugging Face) – Translation models

PyTorch – Model inference

SentencePiece – Tokenization

Frontend

Streamlit – Interactive UI

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/multilingual-translator.git
cd multilingual-translator

2️⃣ Backend Setup (FastAPI)
cd backend
pip install -r requirements.txt


Run the FastAPI server:

uvicorn main:app --reload


Backend will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

3️⃣ Frontend Setup (Streamlit)
cd frontend
streamlit run app.py


Frontend will open at:

http://localhost:8501

🔌 API Usage
Endpoint
POST /translate

Request Body
{
  "text": "こんにちは"
}

Response
{
  "japanese": "こんにちは",
  "english": "Hello",
  "hindi": "नमस्ते"
}

🎨 Streamlit UI Features

Text input for Japanese sentences

Button to trigger translation

Displays English intermediate output

Displays final Hindi translation

Clean and minimal UI

🧪 Example

Input (Japanese):

私は学生です


Output:

English: I am a student
Hindi: मैं एक छात्र हूँ

🏷️ Versioning

v1.0.0 – Initial multilingual translation model (JA → EN → HI)

v1.1.0 – FastAPI backend added

v1.2.0 – Streamlit frontend added

🔮 Future Enhancements

Add more languages (EN → FR, EN → DE, etc.)

Audio input/output (Speech-to-Text & Text-to-Speech)

Authentication & rate limiting

Docker & cloud deployment

Mobile frontend

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a new branch

Commit your changes

Open a pull request

📄 License

This project is licensed under the MIT License.

🙌 Acknowledgements

Hugging Face Transformers

FastAPI

Streamlit

PyTorch
