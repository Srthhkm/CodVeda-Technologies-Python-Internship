def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("File Encryption / Decryption")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Choose option (1/2): ")

    file_name = input("Enter file name: ")
    shift = int(input("Enter shift value: "))

    try:
        with open(file_name, "r") as file:
            content = file.read()

        if choice == "1":
            result = encrypt(content, shift)
            output_file = "encrypted.txt"
        elif choice == "2":
            result = decrypt(content, shift)
            output_file = "decrypted.txt"
        else:
            print("Invalid choice")
            return

        with open(output_file, "w") as file:
            file.write(result)

        print(f"Operation successful. Output saved in {output_file}")

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()
