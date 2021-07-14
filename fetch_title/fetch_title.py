from bs4 import BeautifulSoup as bs
import requests
import sys

class ResultContainer:
    status = None
    message = None
    title = None
    query = None

    def __init__(self, status, message, title, query):
        self.status = status
        self.message = message
        self.title = title
        self.query = query

def fetch_title(url):
    try:
        soup = bs(requests.get(url).text, 'lxml')
        status = 'OK'
        message = 'fetching title success.'
        res = soup.title.string
    except requests.exceptions.MissingSchema as err:
        status = 'ERR'
        message = str(err)
        res = None
    result = ResultContainer(status, message, res, url)
    return result

def main(url):
    status = None
    message = None
    content = fetch_title(url)
    print(content.__dict__)

if __name__ == '__main__':
    url = sys.argv[1]
    content = main(url)