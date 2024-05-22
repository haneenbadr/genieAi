import json
import requests
import sys

# Replace with your actual API key
API_KEY = "Your api key"

text=""

if len(sys.argv)>1:
    text = 'Help with any question i ask about linux bash commands only. other wise if my question is off topic please only say :I’m sorry, I only answer bash specific questions" So my questions is' + sys.argv[1]

else :
    exit()

# Content to be sent
content = {
    "contents": [
        {
            "parts": [
                {
                     "text":text
                }
            ]
        }
    ]
}

# URL for the API endpoint
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

# Set headers
headers = {"Content-Type": "application/json"}

# Send POST request with JSON data
response = requests.post(url, headers=headers, json=content)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
  print(data)

else:
  print("Error:", response.status_code, response.text)

