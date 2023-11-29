from hashlib import blake2b

def get_key(password: str):
    '''Gera um hash (32 bits) da senha passada.

    password (str): Uma string representando uma senha
    '''

    h = blake2b(digest_size=32)
    h.update(password.encode("utf-8"))

    return h.digest()
