def mode():
    print('Deux modes sont disponibles: le mode encoder (1) et le mode décoder (2)')
    choice = input('Veuillez entrer le mode choisi: ')
    try:
        choice = int(choice)
    except ValueError:
        print(f"Le mode choisi ({choice}) n'est pas correct. Veuillez entrer 1 ou 2.")
        exit(2)

    if choice == 1:
        vigenere_cypher_encr()
    elif choice == 2:
        vigenere_cypher_decr()
    else:
        print(f"Le mode choisi ({choice}) n'est pas correct. Veuillez entrer 1 ou 2")
        exit(2)

def message_input():
    message = input("entrez votre message: ")
    return list(message)

def base_key_input():
    key = input('entrez la clef du message: ')
    return list(key)

def key_creation(message, base_key):
    message_length = len(message)
    base_key_length = len(base_key)
    rest = message_length % base_key_length
    temp_key_1 = base_key[:rest]
    multiple = message_length // base_key_length
    key = base_key * multiple
    key.extend(temp_key_1)
    return key

def letter_to_number(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number_list = []
    for char in string:
        number_list.append(alphabet.index(char))
    return number_list

def number_to_letter(numbers):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    characters_list = []
    for number in numbers:
        characters_list.append(alphabet[number])
    return characters_list

def cypher_creation(message, key):
    final_message_number = []
    for i in range(len(message)):
        number = (message[i] + key[i]) % 52
        final_message_number.append(number)
    final_message = number_to_letter(final_message_number)
    final_message = ''.join(final_message)
    return final_message

def decypher_creation(message, key):
    final_message_number = []
    for i in range(len(message)):
        number = (message[i] - key[i]) % 52
        final_message_number.append(number)
    final_message = number_to_letter(final_message_number)
    final_message = ''.join(final_message)
    return final_message

def vigenere_cypher_encr():
    message = message_input()
    key = key_creation(message, base_key_input())
    number_key = letter_to_number(key)
    number_message = letter_to_number(message)
    message_encr = cypher_creation(number_message, number_key)
    print(message_encr)

def vigenere_cypher_decr():
    message = message_input()
    message_encr = letter_to_number(message)
    key = letter_to_number(key_creation(message, base_key_input()))
    message_decr = decypher_creation(message_encr, key)
    print(message_decr)

mode()
