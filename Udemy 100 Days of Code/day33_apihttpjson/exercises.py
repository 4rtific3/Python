import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)

parsed_data = json.dumps(data)
print(parsed_data)