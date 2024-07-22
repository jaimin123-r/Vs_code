import requests

url = "https://youtube138.p.rapidapi.com/video/details/"

querystring = {"id":"kJQP7kiw5Fk","hl":"en","gl":"US"}

headers = {
	"x-rapidapi-key": "Sign Up for Key",
	"x-rapidapi-host": "youtube138.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())