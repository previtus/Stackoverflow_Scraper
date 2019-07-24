# De HTML using Beautify

from bs4 import BeautifulSoup

def html2text(html_string):
    soup = BeautifulSoup(html_string, features="lxml")
    txt = soup.get_text()
    return txt