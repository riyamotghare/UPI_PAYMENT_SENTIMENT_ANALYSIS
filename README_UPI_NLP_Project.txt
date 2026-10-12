UPI Payment Experience Sentiment Analysis Using NLP

Files:
- UPI_Payment_Sentiment_Analysis.ipynb: upload/open in Google Colab and run cells in order.
- upi_payment_reviews_sample.csv: 36 synthetic sample comments (not real customer reviews).
- app.py: Streamlit interface.
- requirements.txt: dependencies.

COLAB:
1. Open https://colab.research.google.com/
2. Upload the notebook.
3. Run each cell in order; upload the sample CSV when prompted.
4. The last cell downloads upi_sentiment_model.joblib and upi_reviews_cleaned.csv.

STREAMLIT:
1. Put app.py, requirements.txt, upi_sentiment_model.joblib, and upi_reviews_cleaned.csv in one folder.
2. Run: pip install -r requirements.txt
3. Run: streamlit run app.py

Important: the supplied CSV is synthetic and is for getting the prototype running. Do not call it a real-world dataset. For stronger research, use a larger genuine, anonymized, labelled review dataset and document its source.
