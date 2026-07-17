import pandas as pd
import nltk
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


nltk.download('stopwords')

data = {
    "review": [
        "I loved the movie! It was fantastic.",
        "The film was terrible and boring.",
        "An excellent performance by the lead actor.",
        "I didn't like the plot, it was too predictable.",
        "The cinematography was stunning.",
        "The soundtrack was amazing!",
        "I found the characters to be very relatable.",
        "The pacing of the movie was off, it dragged in the middle.",
        "The special effects were top-notch.",
        "I was blown away by the visual effects.",
        "The direction was superb.",
        "A masterpiece! Highly recommend it."
    ],
    "sentiment": [
        "positive",
        "negative",
        "positive",
        "negative",
        "positive",
        "positive",
        "positive",
        "negative",
        "positive",
        "positive",
        "positive",
        "positive"
    ]
}

df = pd.DataFrame(data)
print("DataFrame created successfully.")
print(df.head())#top5 reviews and sentiments

#Text Preprocessing
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
stop_words.discard("not")
stop_words.discard("no")
stop_words.discard("nor")

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [
        stemmer.stem(word) 
        for word in tokens if word not in stop_words
    ]
    return ' '.join(tokens)

df['cleaned_review'] = df['review'].apply(clean_text)
print("Text preprocessing completed.")
print(df.head())  # Display the cleaned reviews

#TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned_review'])
y = df['sentiment']
print(X.shape , y.shape)  # Display the shape of the feature matrix

#Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
print("Train-test split completed.")

#Model Training
model = LogisticRegression()
model.fit(X_train, y_train)
print("Model training completed.")

#Model Evaluation
y_pred = model.predict(X_test)
print("Model evaluation completed.")
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print("Sentiment analysis model is ready for predictions.")
print("type review to predict sentiment or type 'exit' to quit.")

while True:
    user_input = input("Review: ")
    if user_input.lower() == 'exit':
        print("Exiting the sentiment analysis. Goodbye!")
        break
    cleaned_input = clean_text(user_input)
    input_vector = vectorizer.transform([cleaned_input])
    prediction = model.predict(input_vector)
    probability = model.predict_proba(input_vector)
    print(f"Predicted Sentiment: {prediction[0]}\n")
    
    if prediction[0] == 'positive':
        print(f"Confidence: {probability[0][1]:.2f}\n")
        print("This review is likely to be positive.\n")
    else:
        print(f"Confidence: {probability[0][0]:.2f}\n")
        print("This review is likely to be negative.\n")


