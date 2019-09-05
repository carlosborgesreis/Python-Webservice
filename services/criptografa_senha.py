import hashlib

def hash_sha256(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def hash_md5(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()