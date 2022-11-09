import copy
from urllib import parse

import requests


def request(url):
    headers = {'Cookie': 'cf_clearance=lA5yHP5M7xR4v4tlIcvvZ.YMqSuAtOkff3RQoW7oing-1650128605-0-150',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        pass


def is_vulnerable(html):
    errors = ['mysql_fetch_array()', 'You have an error in your SQL syntax']
    for error in errors:
        if error in html:
            return True


if __name__ == "__main__":
    url = 'http://www.bancocn.com/cat.php?id=2'
    url_parsed = parse.urlsplit(url)
    params = parse.parse_qs(url_parsed.query)
    for param in params.keys():
        query = copy.deepcopy(params)
        for c in "\"'":
            query[param][0] = c
            new_params = parse.urlencode(query, doseq=True)
            url_final = url_parsed._replace(query=new_params)
            url_final = url_final.geturl()
            html = request(url_final)
            if html:
                if is_vulnerable(html):
                    print('VUNERABLE! {}'.format(param))
                    quit(0)

    print('NOT VULNERABLE!')