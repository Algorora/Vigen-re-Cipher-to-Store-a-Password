def vigenere_encrypt(plaintext, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    ciphertext = ''
    
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    
    for p, k in zip(plaintext, keyword_repeated):
        if p in alphabet:
            p_index = alphabet.index(p)
            k_index = alphabet.index(k)
            c_index = (p_index + k_index) % 26
            ciphertext += alphabet[c_index]
        else:
            ciphertext += p
    
    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    plaintext = ''
    
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    
    for c, k in zip(ciphertext, keyword_repeated):
        if c in alphabet:
            c_index = alphabet.index(c)
            k_index = alphabet.index(k)
            p_index = (c_index - k_index) % 26
            plaintext += alphabet[p_index]
        else:
            plaintext += c
    
    return plaintext

keyword = "KEY"
password = "PASSWORD"

encrypted_password = vigenere_encrypt(password, keyword)
print(f"Encrypted Password: {encrypted_password}")

decrypted_password = vigenere_decrypt(encrypted_password, keyword)
print(f"Decrypted Password: {decrypted_password}")
