from bs4 import BeautifulSoup as bs
import requests
import sys


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
    return (status, message, res)

# def main(url):
#     fetch_title(url)

def main():
    print("Hi")
if __name__ == '__main__':
    # status = ''
    # message = ''
    # url = sys.argv[1]
    # content = main(url)
    # print(content)
    main()