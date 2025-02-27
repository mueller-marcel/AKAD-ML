import pandas as pd
import spacy
from spacy.cli import download

def filter_abstract(df : pd.DataFrame):

    # Download and load the language model
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

    # Define a function to be applied on the Abstract column for the text preparation
    def clean_text(text):
        doc = nlp(text)
        filtered_words = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        return " ".join(filtered_words)

    # Apply the text preparation on the abstract column
    df["Abstract"] = df["Abstract"].apply(clean_text)

    return df