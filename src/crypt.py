from Crypto.Cipher import AES
from hashlib import pbkdf2_hmac
from Padding import appendPadding, removePadding

def _required_padding(a, b = 16, c = 1):
    while a > b:
        c += 1
        b *= c
    return b

def encrypt(plaintext, key, iv):
    if len(plaintext) // 16 or len(plaintext) < 16:
        plaintext = appendPadding(plaintext, _required_padding(len(plaintext)))
    if len(key) < 32:
        key = appendPadding(key, 32)
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode("utf-8"))
    return ciphertext

def decrypt(ciphertext, key, iv):
    if len(key) < 32:
        key = appendPadding(key, 32)
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv)
    plaintext = removePadding((cipher.decrypt(ciphertext)).decode(), _required_padding(len(ciphertext)))
    return plaintext

def hashKey(key, salt):
    hashObj = pbkdf2_hmac("sha256", key.encode("utf-8"), salt, 100000)
    return hashObj