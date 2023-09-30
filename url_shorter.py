import requests

base_url = "https://url-shortener-service.p.rapidapi.com/shorten"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "myapi",
	"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
}

input_url = {"url": input("enter your url > ")}

response = requests.post(base_url, data=input_url, headers=headers)

print('Your new url: ', response.json()['result_url'])
