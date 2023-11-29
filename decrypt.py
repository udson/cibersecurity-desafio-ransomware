# Desencripta um arquivo.

import os, pyaes
from key import get_key


# Cria chave de criptografia
key_32 = get_key("Minha senha")

# Cria o modo de operação
mode = pyaes.AESModeOfOperationCBC(key_32)

# Caminho do arquivo a ser descriptografado
file_path = "./meu_arquivo.txt.troll"

# Abre os arquivos para leitura e escrita
file_in = open(file_path, "rb")
file_out = open(f"{file_path}".replace(".troll", ""), "bw")

# Desencripta o arquivo de entrada
pyaes.decrypt_stream(mode, file_in, file_out)

# Fecha os arquivos
file_in.close()
file_out.close()

# Apaga o arquivo original
if True:
    os.remove(file_path)
