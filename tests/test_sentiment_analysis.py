import unittest
from src.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_analyze_sentiment_positive(self):
        prompt = "This is a positive sentence."
        bot_id = "sentiment-100m"
        response = analyze_sentiment(prompt, bot_id)
        self.assertEqual(response['data']['sentiment'], "positive")

    # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()
