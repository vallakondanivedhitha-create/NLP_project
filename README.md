# 🤖 NLP Applications Project

A collection of Natural Language Processing (NLP) applications built using **Python**, **Hugging Face Transformers**, **PyTorch**, **NLTK**, and **Scikit-Learn**. This project demonstrates both Transformer-based NLP applications and Machine Learning-based text classification for solving real-world language processing tasks.

---

## 📌 Project Overview

This project showcases multiple NLP applications ranging from Question Answering, Text Summarization, and Language Translation using state-of-the-art Transformer models to Sentiment Analysis using traditional Machine Learning techniques.

The project currently includes:

- ✅ Question Answering Chatbot
- ✅ Text Summarization Tool
- ✅ Language Translation Tool
- ✅ Movie Review Sentiment Analysis

All applications run locally and demonstrate different approaches to Natural Language Processing.

---

## 🚀 Features

### 📖 Question Answering Chatbot

- Answers questions based on a given context.
- Uses the DistilBERT Question Answering model.
- Interactive command-line interface.
- Fast and lightweight inference.
- Powered by Hugging Face Transformers.

---

### 📝 Text Summarization

- Generates concise summaries from long paragraphs or articles.
- Uses Facebook's BART Large CNN model.
- Produces human-readable summaries.
- Suitable for articles, reports, and documents.

---

### 🌍 Language Translation

- Translates text between languages.
- Uses Hugging Face Transformer models.
- Supports Neural Machine Translation (NMT).
- Interactive command-line interface.
- Fast and accurate translation generation.

---

### 🎬 Movie Review Sentiment Analysis

- Predicts whether a review is Positive or Negative.
- Text preprocessing using NLTK.
- Stopword removal and stemming.
- Feature extraction using TF-IDF Vectorization.
- Logistic Regression classifier.
- Displays confidence scores for predictions.
- Interactive command-line interface.

---

## 🛠 Technologies Used

### Programming Language

- Python

### NLP Libraries

- Hugging Face Transformers
- NLTK
- Tokenizers

### Deep Learning Frameworks

- PyTorch
- TensorFlow
- tf-keras

### Machine Learning Libraries

- Scikit-Learn
- Pandas

---

## 📂 Project Structure

```text
NLP-Project/
│
├── chatbot/
├── Chatbot.py
├── sentimental.py
├── summarization.py
├── translation.py
└── README.md
```

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/NimmanaJeevanaJyothi/NLP-Project.git
```

Move into the project directory:

```bash
cd NLP-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Question Answering Chatbot

```bash
python Chatbot.py
```

### Example

```text
You: Who created Python?

Chatbot: Guido van Rossum
```

---

## ▶️ Run the Text Summarizer

```bash
python summarization.py
```

### Example

```text
Input:
Artificial Intelligence is transforming healthcare...

Output:
Artificial Intelligence is transforming healthcare by improving diagnosis, automation, and patient care.
```

---

## ▶️ Run the Language Translator

```bash
python translation.py
```

### Example

```text
Input:
Hello, how are you?

Output:
Bonjour, comment allez-vous ?
```

---

## ▶️ Run the Sentiment Analysis System

```bash
python sentimental.py
```

### Example

```text
Review:
The movie was amazing and the acting was outstanding.

Predicted Sentiment:
positive

Confidence:
0.94
```

---

## 🤖 Models Used

### Question Answering

```text
distilbert-base-uncased-distilled-squad
```

### Text Summarization

```text
facebook/bart-large-cnn
```

### Language Translation

```text
Helsinki-NLP/opus-mt-en-fr
```

### Sentiment Analysis

```text
TF-IDF Vectorizer + Logistic Regression
```

---

## ⚙️ NLP Pipeline Used in Sentiment Analysis

1. Text Cleaning
2. Lowercase Conversion
3. Punctuation Removal
4. Stopword Removal
5. Stemming using Porter Stemmer
6. TF-IDF Feature Extraction
7. Logistic Regression Classification
8. Sentiment Prediction with Confidence Score

---

## 📷 Sample Output

### Question Answering

```text
You: Who developed TensorFlow?

Chatbot:
Google
```

---

### Text Summarization

```text
Input:
Artificial Intelligence is one of the fastest growing technologies...

Summary:
Artificial Intelligence is rapidly transforming industries through automation, machine learning, and intelligent decision-making.
```

---

### Language Translation

```text
Input:
Good Morning

Output:
Bonjour
```

---

### Sentiment Analysis

```text
Review:
I absolutely loved this movie. The visuals were incredible.

Predicted Sentiment:
positive

Confidence:
0.91
```

---

## 🎯 Future Improvements

- Conversational AI Assistant
- Named Entity Recognition (NER)
- Emotion Detection
- Machine Translation for Multiple Languages
- Text Generation
- Grammar Correction
- Speech-to-Text
- Text-to-Speech
- Streamlit Web Interface
- Multi-document Summarization
- Deep Learning Sentiment Analysis using BERT

---

## 📚 Learning Outcomes

Through this project, I learned:

- Hugging Face Transformers
- Transformer-based NLP Applications
- Question Answering Pipelines
- Text Summarization Pipelines
- Language Translation Models
- Machine Learning for NLP
- Text Preprocessing Techniques
- TF-IDF Vectorization
- Logistic Regression Classification
- NLTK for NLP Tasks
- PyTorch Integration
- Natural Language Processing Fundamentals

---

## 👩‍💻 Author

**Nimmana Jeevana Jyothi**

GitHub: https://github.com/NimmanaJeevanaJyothi

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.