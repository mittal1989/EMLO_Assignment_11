import requests

url = "http://localhost:80"

url = url + "/find_similarity?text=Cat,Two Cat,Dog,Person,Car"

payload = {}
files=[
  ('image',('1.jpg',open(r'C:/Users/0152013/Desktop/Test/2.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
