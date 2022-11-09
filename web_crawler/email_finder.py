import sys
import re

import requests
from bs4 import BeautifulSoup

TO_CRAWL = []
CRAWLED = set()
EMAILS = []


def request(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
    try:
        response = requests.get(url, headers=header)
        return response.text
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass


def get_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, 'html.parser')
        tags_a = soup.find_all('a', href=True)
        for tag in tags_a:
            link = tag['href']
            if link.startswith('http'):
                links.append(link)

        return links
    except:
        pass


def get_emails(html):
    emails = re.findall(r"\w[\w\.]+\w@\w[\w\.]+\w", html)
    return emails


def craw():
    while True:
        if TO_CRAWL:
            url = TO_CRAWL.pop()
            html = request(url)
            if html:
                links = get_links(html)
                if links:
                    for link in links:
                        if link not in CRAWLED and link not in TO_CRAWL:
                            TO_CRAWL.append(link)

                emails = get_emails(html)
                if emails:
                    for email in emails:
                        if email not in EMAILS:
                            print(email)
                            EMAILS.append(email)

                CRAWLED.add(url)
            else:
                CRAWLED.add(url)
        else:
            print('Done')
            break


if __name__ == '__main__':
    url = sys.argv[1]
    TO_CRAWL.append(url)
    craw()