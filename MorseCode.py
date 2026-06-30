morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


def encode_to_morse(text):
    # Write code here
    encoded_words = []
    text = text.upper().strip()

    for word in text.split():
        encoded_letters = []
        for char in word:
            if char in morse_dict:  # Only encode known characters
                encoded_letters.append(morse_dict[char])
        encoded_words.append(" ".join(encoded_letters))
    
    return " / ".join(encoded_words)
    
txt = input("Give me your text:")
print(encode_to_morse(txt))
