# Sentiment Analysis Model

Welcome to the Sentiment Analysis Model Repository! This repository houses a sentiment analysis model implemented as a REST API, which is launched as part of the all-new under beta Supervised AI's Function API.

## Introduction

The Sentiment Analysis Model is designed to analyze text inputs and predict whether the sentiment expressed within the text is positive, negative, or neutral. Leveraging the power of advanced machine learning techniques, this model provides accurate sentiment analysis results, making it suitable for a wide range of applications, including social media monitoring, customer feedback analysis, and market sentiment analysis.

## Usage

To use the Sentiment Analysis Model, follow the steps outlined below:

1. **Install Dependencies**: Ensure you have the required dependencies installed by running the following command:

pip install -r requirements.txt


2. **Run the API Server**: Start the API server by executing the following command:

python src/sentiment_analysis.py


3. **Make Requests to the API**: Send requests to the API using the provided Function API structure.

## Function API Structure

The Sentiment Analysis Model API follows the Function API structure as part of the Supervised AI's Function API. You can make POST requests to the following endpoint:

POST: https://service.supervised.co/json/call/v2/function


The request body should be formatted as follows:

```json
{
  "prompt": "Your text input here",
  "botId": "sentiment-100m"
}
