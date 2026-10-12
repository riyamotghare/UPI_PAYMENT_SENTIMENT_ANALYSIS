
import streamlit as st
import joblib
import re
from pathlib import Path

st.set_page_config(
    page_title="UPI Sentiment Analysis",
    page_icon="💳",
    layout="centered"
)


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


MODEL_PATH = Path(__file__).parent / "upi_sentiment_model.joblib"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


st.title("💳 UPI Payment Sentiment Analysis")
st.write(
    "Analyze user feedback about UPI payment applications "
    "using Natural Language Processing."
)

if not MODEL_PATH.exists():
    st.error(
        "Model file not found. Place upi_sentiment_model.joblib "
        "in the same folder as app.py."
    )
    st.stop()

try:
    model = load_model()
except Exception as error:
    st.error(f"Could not load the model: {error}")
    st.stop()

review = st.text_area(
    "Enter your UPI review",
    placeholder="Example: My payment failed and money was deducted.",
    height=130
)

if st.button("Analyze Sentiment", type="primary"):
    if not review.strip():
        st.warning("Please enter a review first.")
    else:
        cleaned_review = clean_text(review)

        prediction = model.predict([cleaned_review])[0]

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba([cleaned_review])[0]
            confidence = max(probabilities) * 100
        else:
            confidence = None

        st.subheader("Analysis Result")

        if prediction == "Negative":
            st.error(f"Sentiment: {prediction}")
        elif prediction == "Positive":
            st.success(f"Sentiment: {prediction}")
        else:
            st.info(f"Sentiment: {prediction}")

        if confidence is not None:
            st.write(f"Model confidence: {confidence:.1f}%")

st.divider()
st.caption(
    "Academic project: UPI Payment Experience Sentiment Analysis "
    "Using Natural Language Processing."
)
