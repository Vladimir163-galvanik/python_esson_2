import requests
import jsons

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = jsons.loads(response.text)
print(data)