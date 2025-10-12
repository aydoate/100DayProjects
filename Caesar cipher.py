alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text +=letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    go_again=input("Would you like to go again? Type 'yes' or 'no'\n").lower()
    if go_again=="yes":
        program_start()
    else:
        print("Have a nice day.")
def program_start():
    encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    caesar(original_text, shift_amount, encode_or_decode)

program_start()
