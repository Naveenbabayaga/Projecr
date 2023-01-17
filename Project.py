import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import rollbar

rollbar.init(
  access_token='ad27c3a3a15242619be1caff8a7ae285',
  environment='testenv',
  code_version='1.0'
)
try:
    a - None
    a.hello()
except:
    rollbar.report_exc_info()


def encrypt_image(image_path, key):
    # Open the image file
    with open(image_path, 'rb') as image:
        # Read the image data
        plaintext = image.read()
    
    # Generate a random 96-bit IV
    iv = os.urandom(12)
    # Create a new AES-GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Add additional authentication data (AAD)
    encryptor.authenticate_additional_data(b"header")
    # Encrypt the plaintext
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    # Get the authentication tag 
    tag = encryptor.tag
    # Return the IV and ciphertext
    return iv, ciphertext, tag

def decrypt_image(iv, ciphertext, key, tag):
    # Create a new AES-GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), 
    backend=default_backend())
    decryptor = cipher.decryptor()
    # Add additional authentication data (AAD)
    decryptor.authenticate_additional_data(b"header")
    # Decrypt the ciphertext and pass the authentication tag for verification
    plaintext = decryptor.update(ciphertext) + 
    decryptor.finalize();
    decryptor.verify(tag)
    # Return the plaintext
    return plaintext

# Example usage

# Generate a random 256-bit key
key = os.urandom(32)

# Encrypt the image
result = encrypt_image('Test.jpg', key)
iv, ciphertext, tag = result

# Decrypt the image
print(type(tag))
plaintext = decrypt_image(iv, ciphertext, key, tag)

# Write the decrypted image data to a new file
with open('decrypted_image.jpg', 'wb') as image:
    image.write(plaintext)

# Save the key to a file
with open('key.bin', 'wb') as key_file:
    key_file.write(key)

# Save the IV and tag to a file
with open('iv.bin', 'wb') as iv_file:
    iv_file.write(iv)
with open('tag.bin', 'wb') as tag_file:
    iv_file.write(tag)

# Save the ciphertext to a file
with open('ciphertext.bin', 'wb') as ciphertext_file:
    ciphertext_file.write(ciphertext)

# Read the key from a file
with open('key.bin', 'rb') as key_file:
    key = key_file.read()

# Read the IV and tag from a file
with open('iv.bin', 'rb') as iv_file:
    iv = iv_file.read()
with open('tag.bin', 'rb') as tag_file:  
    tag = iv_file.read()

# Read the ciphertext from a file
with open('ciphertext.bin', 'rb') as ciphertext_file:
    ciphertext = ciphertext_file.read()

# Decrypt the image
plaintext = decrypt_image(iv, ciphertext, key, tag)

# Write the decrypted image data to a new file
with open('decrypted_image.jpg', 'wb') as image:
    image.write(plaintext)