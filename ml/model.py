import json
import pandas as pd
import numpy as np
import string, re
import nltk
import sklearn
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from catboost import CatBoostClassifier # For building catboost model
from xgboost import XGBClassifier
from sklearn.feature_extraction.text import TfidfVectorizer # For vectorizing text data
from sklearn.metrics import accuracy_score
import pickle
import os
import logging

# Set up the logger
logging.basicConfig(level=logging.INFO)

model_address = 'ml/staging-model.pkl'


def preprocess_dataframe(df):
    df['Preprocessed_posts'] = df['posts'].str.lower()
    df['Preprocessed_posts'] = df['Preprocessed_posts'].str.replace(r'https?://[^\s<>"]+|www\.[^\s<>"]+', ' ',
                                                                    flags=re.MULTILINE, regex=True)
    df['Preprocessed_posts'] = df['Preprocessed_posts'].str.replace(r'[^0-9a-z]', ' ', regex=True)
    return df


# Removing stopwords and applying lemmatizer
def remove_stopwords_lemmatizer(post):
    tokens = word_tokenize(post)
    stopwords = nltk.corpus.stopwords.words('english')
    filtered_tokens = [token for token in tokens if token not in stopwords]
    lemmatizer = nltk.WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text


def add_sentiment_column(post):
    sentiment_analyzer = SentimentIntensityAnalyzer()
    scores = sentiment_analyzer.polarity_scores(post)
    if scores["compound"] == 0:
        sentiment = 2
    elif scores["compound"] > 0:
        sentiment = 1
    else:
        sentiment = 0
    return sentiment

def predict_personality(text):

    #Preprocessing the text input(removing stopwords + sentiment)
    data = [text]
    df = pd.DataFrame(data, columns=['posts'])
    df = preprocess_dataframe(df)
    df['Preprocessed_posts'] = df['Preprocessed_posts'].apply(lambda x: remove_stopwords_lemmatizer(x))
    df = df.drop(df[df['Preprocessed_posts'] == ''].index)

    if df.empty:
        return "The text length was not enough for processing!"

    df['sentiment'] = df['Preprocessed_posts'].apply(lambda x: add_sentiment_column(x))

    #loading the model and vectorizer
    pickled_model, loaded_vectorizer = pickle.load(open(model_address, 'rb'))

    #Vectorizing the text data
    vectors_tfidf = loaded_vectorizer.transform(df['Preprocessed_posts'])

    #Combining vectorizers output with sentiment column
    vectors_tfidf_array = vectors_tfidf.toarray()
    input_text = np.column_stack((vectors_tfidf_array, df['sentiment'].to_numpy()))

    #Running the model and getting prediction
    input_text_pred = pickled_model.predict(input_text)

    label_predicted = input_text_pred[0][0]
    labels = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

    return labels[label_predicted], label_predicted

def predict(text):
    logging.info(f"Predicting personality for text: {text}")
    nltk.download('vader_lexicon')
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    logging.info(f"Download is done!")

    personality_predicted, label_predicted = predict_personality(text)
    logging.info(f"Personality predicted: {personality_predicted}")
    logging.info(f"Label predicted: {label_predicted}")

    personality_predicted = {
        "personality_predicted": personality_predicted,
        "label_predicted": int(label_predicted)
    }

    # Return a response
    return personality_predicted
