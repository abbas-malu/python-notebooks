import string
import pandas as pd 
import random

def encrypt(string_to_be_encrpypted):
    """
    Encrpyting String Using Some Algorithm
    """
    main_dict = {
        'character': [],
        'pos_1': [],
        'pos_2': [],
        'pos_3': [],
        'pos_4': [],
    }
    keys = pd.read_csv('crptograph.csv')
    pos_list = ['pos_1','pos_2','pos_3','pos_4']
    for char in keys.character:
        main_dict['character'].append(char)
    for pos in pos_list:
        for i in keys[pos]:
            main_dict[pos].append(i)
    encrypted_string = ''
    for en_ch in string_to_be_encrpypted:
        main_index = main_dict['character'].index(en_ch)
        for pos in pos_list:
            encrypted_string += main_dict['character'][main_dict[pos][main_index]]
        encrypted_string += 'aaa'
    return encrypted_string
def decrypt(string_to_be_decrypted):
    """
    Decrypting a string using some algorithm
    """
    main_dict = {
        'character': [],
        'pos_1': [],
        'pos_2': [],
        'pos_3': [],
        'pos_4': [],
    }
    keys = pd.read_csv('crptograph.csv')
    pos_list = ['pos_1','pos_2','pos_3','pos_4']
    for char in keys.character:
        main_dict['character'].append(char)
    for pos in pos_list:
        for i in keys[pos]:
            main_dict[pos].append(i)
    str_list = string_to_be_decrypted.split('aaa')
    str_list.pop(-1)
    decrypted_string = ''
    # main_index = main_dict['pos_1'].index(main_dict['character'].index(str_list[0][0]))
    # print(main_index)
    for i in str_list:
        main_index = main_dict['pos_1'].index(main_dict['character'].index(i[0]))
        decrypted_string += main_dict['character'][main_index]
    return decrypted_string
my_dec = encrypt('i am great boy 123')
print(decrypt(my_dec))
print(encrypt('i am great boy 123'))