import requests

base_url = "https://url-shortener-service.p.rapidapi.com/shorten"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "f380b72db7msh56a61c6e9441110p19b731jsnf8d601f12a72",
	"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
}

input_url = {"url": input("enter your url > ")}

response = requests.post(base_url, data=input_url, headers=headers)

print('Your new url: ', response.json()['result_url'])