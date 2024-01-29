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
def short_key_length_bruteforce(ciphertext, max_key_length=2):
    for key_length in range(1, max_key_length + 1):
        for i in range(26 ** key_length):  # Try all possible combinations
            possible_key = ""
            for j in range(key_length):
                possible_key += chr(ord('A') + (i // (26 ** j)) % 26)
            decrypted_text = vigenere_decrypt(ciphertext, possible_key)
            print(f"Key Length {key_length}, Key {i + 1:02d}: {decrypted_text}")
def main():
    ciphertext = "WKL"
    print("Ciphertext:", ciphertext)
    print("\nShort Key Length Brute-Force Attack:")
    short_key_length_bruteforce(ciphertext)
if __name__ == "__main__":
    main()
