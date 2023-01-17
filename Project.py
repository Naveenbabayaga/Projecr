import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import rollbar

def encrypt_image(image_path, key):
  
    with open(image_path, 'rb') as image:
        
        plaintext = image.read()
    

    iv = os.urandom(12)
 
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    encryptor.authenticate_additional_data(b"header")
   
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    
    tag = encryptor.tag
    t
    return iv, ciphertext, tag

def decrypt_image(iv, ciphertext, key, tag):

    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), 
    backend=default_backend())
    decryptor = cipher.decryptor()
    
    decryptor.authenticate_additional_data(b"header")
   
    plaintext = decryptor.update(ciphertext) + 
    decryptor.finalize();
    decryptor.verify(tag)
 
    return plaintext

key = os.urandom(32)

result = encrypt_image('Test.jpg', key)
iv, ciphertext, tag = result

print(type(tag))
plaintext = decrypt_image(iv, ciphertext, key, tag)

with open('decrypted_image.jpg', 'wb') as image:
    image.write(plaintext)

with open('key.bin', 'wb') as key_file:
    key_file.write(key)

with open('iv.bin', 'wb') as iv_file:
    iv_file.write(iv)
with open('tag.bin', 'wb') as tag_file:
    iv_file.write(tag)

with open('ciphertext.bin', 'wb') as ciphertext_file:
    ciphertext_file.write(ciphertext)

with open('key.bin', 'rb') as key_file:
    key = key_file.read()

with open('iv.bin', 'rb') as iv_file:
    iv = iv_file.read()
with open('tag.bin', 'rb') as tag_file:  
    tag = iv_file.read()

with open('ciphertext.bin', 'rb') as ciphertext_file:
    ciphertext = ciphertext_file.read()

plaintext = decrypt_image(iv, ciphertext, key, tag)

with open('decrypted_image.jpg', 'wb') as image:
    image.write(plaintext)
