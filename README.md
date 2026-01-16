# Movie Review Sentiment Analysis (Machine Learning)

This is an end-to-end Machine Learning project that classifies movie reviews as **Positive** or **Negative** using Natural Language Processing (NLP) techniques.  
The trained model is deployed as an interactive web application using Streamlit.

## Project Overview

The objective of this project is to build a sentiment analysis system for movie reviews.  
It covers the complete machine learning lifecycle, from text preprocessing and model training to deployment as a web application.

Users can enter a movie review and receive:
- Sentiment prediction (Positive or Negative)
- Confidence score of the prediction


## Machine Learning Approach

### Text Preprocessing
- Convert text to lowercase
- Remove HTML tags and URLs
- Remove punctuation and digits
- Clean and normalize text

### Feature Extraction
- TF-IDF Vectorizer
- Unigrams and Bigrams

### Model
- Logistic Regression

### Hyperparameter Tuning
- RandomizedSearchCV with cross-validation

### Pipeline
- All preprocessing and model steps are combined into a single scikit-learn pipeline
- The trained pipeline is saved using Joblib

## Deployment

- The trained model is deployed as an interactive web application using Streamlit
- Users can input custom movie reviews and receive real-time predictions

## Technologies Used

- Python
- Pandas
- NumPy
- scikit-learn
- NLTK
- Streamlit
- Joblib

