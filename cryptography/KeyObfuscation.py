import math
import hashlib

def letter_to_number(letter):
    temp_list = []
    letter = list(str(letter))
    for i in letter:
        temp_list.append(str(ord(i)))
    temp_list = ''.join(temp_list)
    temp_list = int(temp_list)
    return temp_list

def create_key_1(precedent_key, key):
    key1 = pow(key+precedent_key, 10**1000, 10 ** 20 + 97506748931476587197)
    return key1

def create_key_2(precedent_key, key):
    key2 = precedent_key * int(math.sqrt(key))
    return key2

def create_key_3(precedent_key):
    byte_key_3 = precedent_key.to_bytes((precedent_key.bit_length() + 7) // 8, byteorder='big')
    sha_key_3 = hashlib.sha512()
    sha_key_3.update(byte_key_3)
    key3 = letter_to_number(sha_key_3.digest())
    return key3

def create_key_4(precedent_key):
    test=precedent_key

def key_obfuscation(key, base_key):
    key = letter_to_number(key)
    base_key = letter_to_number(base_key)
    key_number_1 = create_key_1(base_key, key)
    key_number_2 = create_key_2(key_number_1, key)
    key_number_3 = create_key_3(key_number_2)
    final_key = pow(pow(key_number_1 * key_number_2, 100**10000, 10**600)-key_number_3, 100**10000, 10**400+196)
    return final_key


key_input = input('enter the key: ')
key_base = 1938214987
print(key_obfuscation(key_input, key_base))