import requests
import wget
from bs4 import BeautifulSoup

def main():
    base_url = 'http://www.cs.unm.edu/~saia/classes/527-s18/'
    fname_downloaded_list = '.downloaded.txt'
    r = requests.get(base_url)
    # print(r.status_code)

    soup = BeautifulSoup(r.content, 'html.parser')

    lecture_links = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('lec/'):
            lecture_links.add(base_url + href)
    # print(len(lecture_links), lecture_links)

    already_downloaded = set()
    try:
        with open(fname_downloaded_list, 'r') as f:
            for line in f:
                already_downloaded.add(line.strip())
    except FileNotFoundError:
        open(fname_downloaded_list, 'w+')
        print("Creating file {}".format(fname_downloaded_list))

    # print(len(already_downloaded),already_downloaded)

    yet_to_download = lecture_links - already_downloaded
    # print(len(yet_to_download), yet_to_download)

    # download the lectures, and update .downloaded.txt
    with open(fname_downloaded_list, 'a') as f:
        for url in yet_to_download:
            filename = wget.download(url)
            print(" Downloaded ", filename)
            f.write("{}\n".format(url))


if __name__ == '__main__':
    main()
