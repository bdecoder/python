#THIS CODE IS STILL IN DEV


import numpy as np

def letter_to_number(string):
    alphabet = ['¤', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', ' ']
    number_list = []
    for char in string:
        number_list.append(alphabet.index(char))
    return number_list

def number_to_letter(numbers):
    alphabet = ['¤', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', ' ']
    characters_list = []
    for number in numbers:
        characters_list.append(alphabet[number])
    return characters_list

def message_input():
    message = input("entrez votre message: ")
    return list(message)

def message_size(message):
    message_length = len(message)
    message_check = message_length % 3
    if message_check == 0:
        message = message
    elif message_check == 1:
        message.append(26)
        message.append(26)
    elif message_check == 2:
        message.append(26)
    return message

def cut_message(message):
    return [message[i:i + 3] for i in range(0, len(message), 3)]


def matrice_multiplication(vector):
    number_message = []
    matrice = np.array([[49, 943, 929], [903, 196, 472], [345, 806, 149]])
    for i in range(len(vector)):
        temp = np.dot(matrice, vector[i])
        temp = temp % 27
        number_message.append(temp)
    number_message = number_message
    return number_message

def hill_cypher_encr():
    message = list(message_input())
    message_number = letter_to_number(message)
    message_before_encr = message_size(message_number)
    message_vector = cut_message(message_before_encr)
    number_message_encr = matrice_multiplication(message_vector)
    message_encr = ''.join(number_to_letter(number_message_encr))
    print(message_encr)

hill_cypher_encr()
