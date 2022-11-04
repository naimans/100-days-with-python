alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encode_text = ""
  for letter in text:
    new_position = alphabet.index(letter) + shift
    if new_position >= 26:
      new_position -= 26
      en_letter = alphabet[new_position]
    else:
      en_letter = alphabet[new_position]
    encode_text = ''.join((encode_text,en_letter))
  print(f"The encoded text is {encode_text}")

def decrypt(text, shift):
  decode_text = ""
  for letter in text:
    new_position = alphabet.index(letter) - shift
    en_letter = alphabet[new_position]
    decode_text += en_letter
  print(f"The decoded text is {decode_text}")

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else:
  print("You typed it worng. Please check spelling mistake")