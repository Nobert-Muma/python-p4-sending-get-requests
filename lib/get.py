import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url)

json_content = json.loads(response.text)

print(json.dumps(json_content, indent=4))

# import requests
# url='https://learn-co-curriculum.github.io/json-site-example/'
# response=requests.get(url)
# print(response.text)