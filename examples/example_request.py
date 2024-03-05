import requests

url = 'http://service.supervised.co/json/call/v2/function'
headers = {
    'Content-Type': 'application/json',
    'Auth': 'Bearer $YourAPIKey'
}
data = {
  "prompt": "Wow, D-ID Agents sounds like an incredibly innovative solution! The ability to create personalized digital people who can engage in real-time conversations is groundbreaking. I'm particularly impressed by the use of advanced AI technology like retrieval augmented generation (RAG) to ensure swift and accurate responses, mimicking natural human interaction.",
  "botId": "sentiment-100m"
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
