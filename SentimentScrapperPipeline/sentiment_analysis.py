import pandas as pd
import numpy as np
import time
pd.set_option('display.max_columns', None)
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')


def sentiment():
	# Initialize the Sentiment Intensity Analyzer
	sia = SentimentIntensityAnalyzer()
	# Analyze sentiment of each comment
	def analyze_sentiment(comment):
		scores = sia.polarity_scores(comment)
		if scores['compound'] > 0.05:
			return 'Positive'
		elif scores['compound'] < -0.05:
			return 'Negative'
		else:
			return 'Neutral'

	data=pd.read_csv('/home/khalil/vs_workspace/ETL_project/data.csv')
	# Apply the sentiment analysis
	data['sentiment'] = data['comments'].apply(analyze_sentiment)
	data.to_csv('/home/khalil/vs_workspace/ETL_project/data_with_sent1.csv', index=False)
		
