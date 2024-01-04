import hashlib

def hash_string(string:str):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()
