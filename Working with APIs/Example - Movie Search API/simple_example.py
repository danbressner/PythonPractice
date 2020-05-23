import requests

url = "https://movieservice.talkpython.fm/api/search/away"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text.encode('utf8'))
# print(response.json())

