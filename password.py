import hashlib

def encrypt_password(password):
    sha256=hashlib.sha256()


    sha256.update(password.encode('utf-8'))

    encrypt_password=sha256.hexdigest()

    return encrypt_password

def decrypt_password(encrypt_password):
    sha256=hashlib.sha256()


    sha256.update(encrypt_password.encode('utf-8'))

    decrypt_password=sha256.digest()

    return decrypt_password

password="JAIMIN123R"
encrypt_password=encrypt_password(password)
decrypt_password=decrypt_password(encrypt_password)
print("original password:",password)
print("encrypted password:",encrypt_password)
print("again original password :",decrypt_password)