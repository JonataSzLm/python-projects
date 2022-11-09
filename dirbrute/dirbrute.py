import sys

import requests


def brute(host, wordlist):
    for word in wordlist:
        try:
            url = '{}/{}'.format(host, word.strip())
            response = requests.get(url)
            code = response.status_code
            if code != 404:
                print('{} -- {}'.format(url, code))
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass


if __name__ == '__main__':
    host = sys.argv[1]
    name_wordlist = sys.argv[2]

    with open(name_wordlist, 'r') as file:
        wordlist = file.readlines()
        brute(host, wordlist)

