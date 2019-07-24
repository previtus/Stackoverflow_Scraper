# Using library: https://github.com/lucjon/Py-StackExchange
# easy_install Py-StackExchange


import stackexchange

API = ""
with open('key.txt', 'r') as apifile:
    API=apifile.read().replace('\n', '')

print(stackexchange)



site = stackexchange.Site(stackexchange.SignalProcessing, API)
site.be_inclusive()


questions = site.recent_questions(pagesize=10, filter='_b',)

cur = 1
for question in questions[:10]:
    print('#%2d %3d  %3d  %3d \t%s' % (cur, question.score, len(question.answers), question.view_count, question.title))
    cur += 1

    question_body = question.body # needs to be de-HTML'd

    print("\t\t\t Body of size", len(question_body), "with", len(question.answers), "answers. Tags = ", question.tags)

