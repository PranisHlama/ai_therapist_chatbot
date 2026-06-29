import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

filepath = "./dataset/conversations_training.json"
with open(filepath, "r", encoding="utf-8") as file:
    data = json.load(file)

def load_qa_dataset():
    df = pd.DataFrame(data)
    df = df.dropna(subset=["input", "output"])
    df["input"] = df["input"].astype(str)
    df["output"] = df["output"].astype(str)
    return df

def find_best_match(user_question):
    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vector, question_vectors).flatten()

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    return df.iloc[best_index], best_score

def get_dataset_reply(user_question, min_score=0.2):
    match, score = find_best_match(user_question)

    if score < min_score:
        return "I could not find a close answer in the dataset. Try asking in a different way."
    
    return match["output"]

df = load_qa_dataset()
# print(df.sample(5))

# Seperate input and output
X_text = df["input"]
y = df["output"]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000,
    ngram_range=(1,2)
)

# Convert input text into TF-IDF numbers
question_vectors = vectorizer.fit_transform(X_text)
# print(question_vectors.shape)