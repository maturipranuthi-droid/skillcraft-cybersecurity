def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
mode = input("Encrypt or decrypt? ").lower()

if mode in ["encrypt", "decrypt"]:
    output = caesar_cipher(message, shift, mode)
    print("Result:", output)
else:
    print("Invalid mode.")