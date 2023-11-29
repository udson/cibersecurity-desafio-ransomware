# Encripta um arquivo utilizando um texto como senha.

import os, pyaes
from key import get_key


# Cria chave de criptografia
key_32 = get_key("Minha senha")

# Cria o modo de operação da função de criptografia
mode = pyaes.AESModeOfOperationCBC(key_32)

# Caminho do arquivo a ser criptografado
file_path = "./meu_arquivo.txt"

# Abre os arquivos para leitura e escrita
file_in = open(file_path, "rb")
file_out = open(f"{file_path}.troll", "bw")

# Encripta o arquivo de entrada
pyaes.encrypt_stream(mode, file_in, file_out)

# Fecha os arquivos
file_in.close()
file_out.close()

# Apaga o arquivo original
os.remove(file_path)