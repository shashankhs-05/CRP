def vigenere_decrypt(ciphertext, key):
    decrypted_text = ''
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_length]
            decrypted_char = chr((ord(char) - shift - ord(key_char) + 26) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
def find_repeated_key_patterns(ciphertext, key_length):
    key_patterns = [''] * key_length
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_patterns[i % key_length] += char
    return key_patterns
def main():
    ciphertext = "WKLVLSWOWPHVVDJH"
    key_length = 3
    repeated_key_patterns = find_repeated_key_patterns(ciphertext, key_length)
    print("Possible repeated key patterns:", repeated_key_patterns)
    for pattern in repeated_key_patterns:
        potential_key = ''.join([chr((ord(char) - ord('A')) % 26 + ord('A')) for char in pattern])
        decrypted_text = vigenere_decrypt(ciphertext, potential_key)
        print(f"Decrypted text using potential key '{potential_key}': {decrypted_text}")

if __name__ == "__main__":
    main()
