
import streamlit as st
import joblib
import re
import string
from sklearn.base import BaseEstimator, TransformerMixin


from nltk.corpus import stopwords



import re
import string
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords

class TextCleaningTransformer(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass   # NOTHING non-picklable here

    def fit(self, X, y=None):
        self.stop_words = set(stopwords.words('english'))
        return self

    def transform(self, X):
        cleaned_text = []

        for txt in X:
            if not isinstance(txt, str):
                cleaned_text.append("")
                continue

            txt = txt.lower()
            txt = re.sub(r'<.*?>', '', txt)
            txt = re.sub(r'http\S+|www\S+', '', txt)
            txt = txt.translate(str.maketrans('', '', string.punctuation))
            txt = ''.join([i for i in txt if not i.isdigit()])
            txt = ''.join([i for i in txt if i.isascii()])

            words = txt.split()
            words = [w for w in words if w not in self.stop_words]

            cleaned_text.append(' '.join(words))

        return cleaned_text


import streamlit as st
import joblib

# Load trained pipeline
model = joblib.load("sentiment_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Movie Review Sentiment Analysis",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    textarea {
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align: center;'>🎬 Movie Review Sentiment Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Enter a movie review and find whether it is Positive or Negative</p>",
    unsafe_allow_html=True
)

st.write("---")

# Input text
review = st.text_area(
    "✍️ Enter your review:",
    height=150,
    placeholder="Example: This movie was absolutely fantastic!"
)

# Predict button
if st.button("🔍 Analyze Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review.")
    else:
        prediction = model.predict([review])[0]
        probability = model.predict_proba([review])[0]

        if prediction == 1:
            st.success("😊 Positive Review")
            st.write(f"**Confidence:** {probability[1]*100:.2f}%")
        else:
            st.error("😞 Negative Review")
            st.write(f"**Confidence:** {probability[0]*100:.2f}%")

st.write("---")

st.markdown(
    "<p style='text-align: center;'>Built using NLP, TF-IDF & Logistic Regression</p>",
    unsafe_allow_html=True
)
