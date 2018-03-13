import requests
from bs4 import BeautifulSoup

def main():
    base_url = 'http://www.cs.unm.edu/~saia/classes/527-s18/'
    r = requests.get(base_url)
    print(r.status_code)

    soup = BeautifulSoup(r.content, 'html.parser')

    lecture_links = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('lec/'):
            lecture_links.add(base_url + href)
    print(len(lecture_links), lecture_links)

    already_downloaded = set()
    with open('.downloaded.txt', 'r') as f:
        for line in f:
            already_downloaded.add(line.strip())
    print(len(already_downloaded),already_downloaded)

if __name__ == '__main__':
    main()
