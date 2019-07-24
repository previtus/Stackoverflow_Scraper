import requests
import json

page = "info" # basic statistics
page = "questions" # questions

BASEURL = "https://api.stackexchange.com/2.2/"+page

API = ""
with open('key.txt', 'r') as apifile:
    API=apifile.read().replace('\n', '')
print("|"+API+"|")

params = {
  "site" : "gamedev",
  "key" : API # <= 10k queries daily, otherwise only 300
}

r = requests.get(BASEURL, params=params)
parsed = r.json()
print(json.dumps(parsed, indent=4, sort_keys=True))
# Results are in "items"
