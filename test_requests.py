import requests
import json

page = "info" # basic statistics
page = "questions" # questions

# Use data.stackexchange.com, select a page and then:
# SELECT * FROM Posts WHERE AnswerCount >= 1
# to get lists of post ids for:

page = "questions/28963" # specific question
# "What are the benefits of the different cylinder caps?"


BASEURL = "https://api.stackexchange.com/2.2/"+page

API = ""
with open('key.txt', 'r') as apifile:
    API=apifile.read().replace('\n', '')

params = {
  "site" : "blender",
  "key" : API, # <= 10k queries daily, otherwise only 300
  #"filter" : "withbody",
  "filter" : "!-y(KwOdKR5Ga7mmruVArx2SJykc-M)3jKiDQBk1fq", # with body and answers
}

r = requests.get(BASEURL, params=params)
parsed = r.json()
print(json.dumps(parsed, indent=4, sort_keys=True))
# Results are in "items"

question_title = parsed["items"][0]["title"]
question_body = parsed["items"][0]["body"]

print(question_title)
print(question_body)

answer_bodies = [a["body"] for a in parsed["items"][0]["answers"]]

print(answer_bodies)

# Remove html!
