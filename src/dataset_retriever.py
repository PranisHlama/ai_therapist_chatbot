import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

filepath = "../dataset/conversations_training.json"
with open(filepath, "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)
# print(df.head(5))

# Seperate input and output
X_text = df["input"]
y = df["output"]

# Create TF-IDF Vectorizer
tfidf = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    max_features=5000,
    ngram_range=(1,2)
)

# Convert input text into TF-IDF numbers
X_tfidf = tfidf.fit_transform(X_text)
print(X_tfidf.shape)