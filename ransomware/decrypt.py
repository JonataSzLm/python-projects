import pyaes

KEY = b'0123456789123456'
filename = 'imagem.png.pyransom'

with open(filename, 'rb') as file:
    conteudo = file.read()

decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(conteudo)

new_filename = filename.replace('.pyransom', '')
with open(new_filename, 'wb') as file:
    file.write(decrypt_data)