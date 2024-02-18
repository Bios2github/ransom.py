import os

# Import the encryption function from the previous example
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        file_data = file.read()

    key_bytes = key.encode('utf-8')
    
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key_bytes), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def encrypt_folder(folder_path, output_folder, key):
    # Create the output folder if it doesn't exist
    os.makedirs( output_folder, exist_ok=True)
    folder_path="/Desktop/Blogs"
    # Iterate through all files in the folder
    for filename in os.listdir("/Desktop/Blogs"):
        input_file = os.path.join(folder_path, filename)
        output_file = os.path.join(output_folder, f"encrypted_{filename}")

        # Encrypt each file
        encrypt_file(input_file, output_file, key)

        print(f"File '{input_file}' encrypted and saved to '{output_file}'.")

# Specify the folder paths and the encryption key
input_folder = "enter/file/to/encrypt"
output_folder = "/enter/file/to/save"
key = "ThisIsASecretKey!"

# Call the encrypt_folder function
encrypt_folder(input_folder, output_folder, key)
