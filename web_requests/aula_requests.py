import requests

cabecalho = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
             "Cookie": "cf_clearance=FfkI7t0TwtpeUVUIgg3raZWD.SOAaVFtTsoGtJ8YXbA-1649530699-0-250; cf_chl_prog=b; cf_chl_rc_m=1; PHPSESSID=ce8soiv32a95t1grdlml3mbo81"}

dados = {'user': 'admin', 'password': 'senhafoda'}

resposta = requests.post('http://www.bancocn.com/admin/index.php', headers=cabecalho, data=dados)
html = resposta.text
print(html)
