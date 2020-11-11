import string
import pandas as pd
import random

main_dict = {
    'character': [],
    'pos_1': [],
    'pos_2': [],
    'pos_3': [],
    'pos_4': [],
}
char_group = [string.ascii_lowercase, string.ascii_uppercase,
              string.digits, string.punctuation, string.whitespace]
all_char = ''
for i in char_group:
    all_char += i
for char_list in char_group:
    for char in char_list:
        main_dict['character'].append(char)
while len(main_dict['pos_1']) != 100:
    print(len(main_dict['pos_1']))
    pos_1 = random.randint(0, len(all_char)-1)
    pos_2 = random.randint(0, len(all_char)-1)
    pos_3 = random.randint(0, len(all_char)-1)
    pos_4 = random.randint(0, len(all_char)-1)
    all_pos = [(pos_1 not in main_dict['pos_1']), (pos_2 not in main_dict['pos_2']),
    (pos_3 not in main_dict['pos_3']), (pos_4 not in main_dict['pos_4'])]
    if all(all_pos):
        main_dict['pos_1'].append(pos_1)
        main_dict['pos_2'].append(pos_2)
        main_dict['pos_3'].append(pos_3)
        main_dict['pos_4'].append(pos_4)

for i in main_dict:
    print(len(main_dict[i]))
print(main_dict)
