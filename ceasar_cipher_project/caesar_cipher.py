alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(encode_decode, original_text, shift_amount):
    cipher_text = ""
    for char in original_text:
        
        # Handle not letters
        if char in alphabet:
            index = alphabet.index(char)
            
            # Change direction if is encode or decode
            if encode_decode == "encode":
                shift_index = index + shift_amount
            else:
                shift_index = index - shift_amount
            
            # Handle index outside the list
            if shift_index >= 25:
                shift_index -= 26 * (int(shift_index / 26))


            cipher_text += alphabet[shift_index]
        # Handle other character not letters
        else:
            cipher_text += char

    print(f"Here is your {encode_decode}d text: {cipher_text}")

caesar(original_text=text, shift_amount=shift, encode_decode=direction)

continue_with_cipher = input("Type 'Y' if you want to go again. Otherwise, type 'N'\n").lower()

while continue_with_cipher != "n":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_decode=direction)

    continue_with_cipher = input("Type 'Y' if you want to go again. Otherwise, type 'N'\n").lower()

print("Bye")