import pickle
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
import os

base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
stemming_dir = os.path.abspath(os.path.join(base_dir, 'static/data/stemming_sms.xlsx'))
model_dir = os.path.abspath(os.path.join(base_dir, 'static/data/naive_bayes_pickle_model.pkl'))

stem_word = pd.read_excel(stemming_dir)
stem_word = stem_word.sort_values(by=['text_stemming'])

with open(model_dir, 'rb') as file:
    pickle_model = pickle.load(file)

def pred(text):
    stemmer = StemmerFactory().create_stemmer()
    stem = stemmer.stem(text)

    vectorizer = TfidfVectorizer(max_features=1000, decode_error='ignore')
    vectorizer.fit(stem_word['text_stemming'])

    class_pred = pickle_model.predict(vectorizer.transform([stem]))
    if class_pred == 0:
        pred = 'Normal'
        status = 'text-success'
    elif class_pred == 1:
        pred = 'Penipuan'
        status = 'text-danger'
    else:
        pred = 'Promo'
        status = 'text-warning'
    return pred, status
