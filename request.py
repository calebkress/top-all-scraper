import requests

response = requests.get('http://www.reddit.com/r/all/top/')

print(response)