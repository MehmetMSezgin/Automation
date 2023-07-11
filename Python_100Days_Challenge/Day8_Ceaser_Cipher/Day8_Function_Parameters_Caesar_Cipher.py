from Day8_Cipher_Art import logo

'''def my_function(Parameter):
    print(Parameter)
my_function("Argument")


def positional_argument(first, second):
    print("x")
positional_argument("1", "2")


def keyword_argument(first, second):
    print(first)
keyword_argument(second="2", first="1")'''

'''def primeNumberChecker(number):
    if number==0 or number==1:
        print("Invalid")
        exit()

    counter = 0
    for i in range(1, (number+1)):
        if number % i == 0:
            counter += 1

    if counter > 2:
        print(f"{number} is NOT a prime number")
    elif counter <= 2:
        print(f"{number} is a prime number")


userInput = int(input("Enter a number \n"))
primeNumberChecker(userInput)'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceaser_cipher(direction_way, message, shift_no):
    message_as_list = []
    for letter in message:
        message_as_list.append(letter)

    if direction_way == "encode":
        encode(message_as_list, shift_no)
    elif direction_way == "decode":
        decode(message_as_list, shift_no)
    else:
        print("Invalid request")
        exit()


def encode(txt, no):
    encrypted_txt_as_list = []
    letter_location = 0
    new_letter_location = 0

    for i in range(0, len(txt)):
        for x in range(0, 26):
            if txt[i] == alphabet[x]:
                letter_location = x
            new_letter_location = letter_location + no
        txt[i] = alphabet[new_letter_location]
        encrypted_txt_as_list.append(txt[i])
    print(encrypted_txt_as_list)

    encrypted_txt = ""
    for letter in encrypted_txt_as_list:
        encrypted_txt += letter

    print(encrypted_txt)


def decode(txt, no):
    decrypted_txt_as_list = []
    letter_location = 0
    new_letter_location = 0

    for i in range(0, len(txt)):
        for x in range(0, 26):
            if txt[i] == alphabet[x]:
                letter_location = x
            new_letter_location = letter_location - no
            if new_letter_location < 0:
                new_letter_location += 26
        txt[i] = alphabet[new_letter_location]
        decrypted_txt_as_list.append(txt[i])
    print(decrypted_txt_as_list)

    decrypted_txt = ""
    for letter in decrypted_txt_as_list:
        decrypted_txt += letter

    print(decrypted_txt)


print(logo)
flag = True

while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser_cipher(direction, text, shift)

    answer = (input("Do you want to continue? y/n \n")).lower()
    if answer == "n":
        print("Goodbye !!!")
        flag = False
