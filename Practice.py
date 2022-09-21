import json
import requests
city=input("Enter city name\n")
response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=81df7a779fa64411b06043ea088bd8c5")
data=response.text
parse_json=json.loads(data)
print(data)

