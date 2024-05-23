MORSE_CODE_DICT: dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ':' '}

def encrypt(message) -> str:
    """Translate a message to Morse code."""
    message_to_list: list = list(message.upper())
    encrypted_message: list = []
    for letter in message_to_list:
        try:
            encrypted_message.append(MORSE_CODE_DICT[letter])
        except KeyError:
            encrypted_message.append('?')
    new_message: str = "".join(encrypted_message)
    return new_message


def main() -> None:
    """Main function to run the Morse code translator."""
    print("Welcom in Text to Morse Code translator.")
    turn_on: bool = True

    while turn_on:

        mode_type: str = input("What would you like to do 1) Translate, 2) End? (Type 1 or 2): ")

        if mode_type == "1":
            message: str = input("Enter your message here: ")
            encrypted_message: str = encrypt(message)
            print("Enencrypted message: ",encrypted_message)
        elif mode_type == "2":
            turn_on = False
        else:
            print("Error, pleas type 1 or 2")

if __name__ == '__main__':
    main()