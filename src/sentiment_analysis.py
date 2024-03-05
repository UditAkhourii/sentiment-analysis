from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/json/call/v2/function', methods=['POST'])
def analyze_sentiment():
    data = request.json
    prompt = data['prompt']
    bot_id = data['botId']
    # Perform sentiment analysis here
    # Replace this with your sentiment analysis logic
    sentiment = "positive"  # Dummy result
    response = "I'm glad you enjoyed the D-ID Agents solution! It's an exciting development in the world of AI and human-machine interaction. If you have any questions or need any assistance, feel free to ask."
    return jsonify({
        "success": True,
        "data": {
            "sentiment": sentiment,
            "completion": response
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
