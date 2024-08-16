# Vigenère Cipher

# Overview
The Vigenère cipher is a classic encryption algorithm that uses a series of Caesar ciphers based on the letters of a keyword. This repository provides a simple implementation of the Vigenère cipher in Python, demonstrating how to encrypt and decrypt text using this historical method.

# Purpose
This project aims to illustrate the Vigenère cipher's encryption and decryption process. While not suitable for secure applications in modern contexts, it serves as an educational example of how historical encryption techniques work.

# How It Works

## Encryption:

-Uses a keyword to determine the shift for each letter in the plaintext.
-Converts each letter of the plaintext and keyword to their respective positions in the alphabet.
-Encrypts by shifting the plaintext letter according to the keyword letter.
## Decryption:

-Uses the same keyword to reverse the encryption process.
-Converts the ciphertext back to plaintext using the keyword.

# How to Run

## Clone the Repository

```sh
https://github.com/Algorora/Vigenere-Cipher-to-Store-a-Password.git
cd vigenere-cipher
```

## Run the Code

Ensure you have Python 3.x installed. Run the script using:

```zh
python vigenere_cipher.py
```
Expected Output
```zh
Encrypted Password: ZEQCAMBH
Decrypted Password: PASSWORD
```


# Disclaimer
This code is provided for educational purposes only. The Vigenère cipher is not secure by modern standards and should not be used for actual cryptographic purposes. For secure applications, consider using contemporary encryption algorithms and hashing techniques.
