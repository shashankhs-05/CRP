def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_length]
            encrypted_char = chr((ord(char) + ord(key_char) - 2 * shift) % 26 + shift)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext
def known_plaintext_attack(ciphertext, known_plaintext):
    key = ''
    for i, char in enumerate(known_plaintext):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = chr((ord(ciphertext[i]) - ord(char) + 26) % 26 + shift)
            key += key_char
    return key
def main():
    known_plaintext = "HELLO"
    ciphertext = vigenere_encrypt(known_plaintext, "KEY")
    deduced_key = known_plaintext_attack(ciphertext, known_plaintext)
    decrypted_text = vigenere_encrypt(ciphertext, deduced_key)
    print("Known Plaintext:", known_plaintext)
    print("Ciphertext:", ciphertext)
    print("Deduced Key:", deduced_key)
    print("Decrypted Text using Deduced Key:", decrypted_text)
if __name__ == "__main__":
    main()
