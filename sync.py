import requests
from bs4 import BeautifulSoup

def main():
    base_url = 'http://www.cs.unm.edu/~saia/classes/527-s18/'
    r = requests.get(base_url)
    print(r.status_code)
if __name__ == '__main__':
    main()
