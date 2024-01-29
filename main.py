import string

def frequency_analysis(ciphertext):
    frequencies = {char: 0 for char in string.ascii_uppercase}
    total_letters = 0
    for char in ciphertext:
        if char.isalpha():
            frequencies[char.upper()] += 1
            total_letters += 1
    relative_frequencies = {char: freq / total_letters for char, freq in frequencies.items()}
    return relative_frequencies
def main():
    ciphertext = "WKLVLVSDUWPHVVDJH"
    frequencies = frequency_analysis(ciphertext)
    print("Ciphertext:", ciphertext)
    print("\nFrequency Analysis:")
    for char, freq in frequencies.items():
        print(f"{char}: {freq:.3f}")
if __name__ == "__main__":
    main()
