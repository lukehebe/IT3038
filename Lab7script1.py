import requests

url = 'https://example.com'  # Replace with your desired website URL
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
