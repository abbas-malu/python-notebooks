import string


class Enc_Dec():
    """
    String Encryptor
    """

    def encrypt(self, string_enc: str, encryption_level: int):
        lower = list(string.ascii_lowercase.lstrip('a')) + \
            list(string.ascii_lowercase.rstrip('z'))
        upper = list(string.ascii_uppercase.lstrip('A')) + \
            list(string.ascii_uppercase.rstrip('Z'))
        digit = list(string.digits.lstrip('0')) + list(string.digits.rstrip('9'))
        punc = list(string.punctuation.lstrip('!')) + list(string.punctuation.rstrip('~'))
        space = [' ','#010', '#020','#030']
        compt = {
            'lower': lower,
            'upper': upper,
            'digit': digit,
            'space': space,
            'punc' : punc,

        }
        def check_type(character: str):
            """
            Checking Type Of Character
            """
            if character.isupper():
                return 'upper'
            elif character.islower():
                return 'lower'
            elif character.isspace():
                return 'space'
            elif character in string.punctuation:
                return 'punc'
            else:
                return 'digit'

        def parse(level):
            """
            Parsing Encryption Level
            """
            return level*2
        while True:
            try:
                if encryption_level == 1 or encryption_level == 2 or encryption_level == 3:
                    level = parse(encryption_level)
                    out_str = ''
                    for char in string_enc:
                        enc_lst = compt[check_type(char)]
                        if check_type(char)=='upper' or check_type(char)=='lower' or check_type(char)=='digit' or check_type(char)=='punc':
                            out_str += enc_lst[enc_lst.index(char)+encryption_level*2]
                            pass
                        else:
                            out_str += enc_lst[enc_lst.index(char)+encryption_level]
                    return out_str
                else:
                    print(
                        'Invalid Arguement For Encryption Value. Expected values 1, 2 or 3.')
            except:
                pass
    def decrypt(self, string_enc: str, encryption_level: int):
            lower = list(string.ascii_lowercase.lstrip('a')) + \
                list(string.ascii_lowercase.rstrip('z'))
            upper = list(string.ascii_uppercase.lstrip('A')) + \
                list(string.ascii_uppercase.rstrip('Z'))
            digit = list(string.digits.lstrip('0')) + list(string.digits.rstrip('9'))
            punc = list(string.punctuation.lstrip('!')) + list(string.punctuation.rstrip('~'))
            space = [' ','#010', '#020','#030']
            compt = {
                'lower': lower,
                'upper': upper,
                'digit': digit,
                'space': space,
                'punc' : punc,

            }
            def check_type(character: str):
                """
                Checking Type Of Character
                """
                if character.isupper():
                    return 'upper'
                elif character.islower():
                    return 'lower'
                elif character.isspace():
                    return 'space'
                elif character in string.punctuation:
                    return 'punc'
                else:
                    return 'digit'

            def parse(level):
                """
                Parsing Encryption Level
                """
                return level*2
            while True:
                try:
                    if encryption_level == 1 or encryption_level == 2 or encryption_level == 3:
                        level = parse(encryption_level)
                        out_str = ''
                        for char in string_enc:
                            enc_lst = compt[check_type(char)]
                            if check_type(char)=='upper' or check_type(char)=='lower' or check_type(char)=='digit' or check_type(char)=='punc':
                                out_str += enc_lst[enc_lst.index(char)-encryption_level*2]
                                pass
                            else:
                                out_str += enc_lst[enc_lst.index(char)-encryption_level]
                        return out_str
                    else:
                        print(
                            'Invalid Arguement For Encryption Value. Expected values 1, 2 or 3.')
                except:
                    pass


if __name__ == "__main__":
    x = Enc_Dec()
    print(x.encrypt('abbas_malu_123', 1))
    print(x.decrypt('cddcu{ocnw{345', 1))
    lower = list(string.ascii_lowercase.lstrip('a')) + \
                list(string.ascii_lowercase.rstrip('z'))
    print(lower)
    print(lower[lower.index('c')-2])
