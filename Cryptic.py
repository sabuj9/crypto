import hashlib

# a to m|  1   2     3    4    5    6    7    8    9   10    11   12   13
item_1 = ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# n to z| 14   15   16   17   18   19   20   21   22   23    24   25   26
item_2 = ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"]
# a to m|  1   2     3    4    5    6    7    8    9   10    11   12   13
item_3 = ["4", "8", "c", "d", "3", "f", "9", "h", "1", "j", "k", "l", "m"]
# n to z| 14   15   16   17   18   19   20   21   22   23    24   25   26
item_4 = ["n", "0", "p", "q", "2", "5", "7", "u", "v", "w", "x", "y", "z"]
# (a to m) a    b    c    d    e    f    g    h    i    j    k    l    m
item_5 = ["4", "8", "(", "δ", "3", "}", "9", "#", "!", "]", "X", "1", "ψ"]
# (n to z) n    o    p    q    r    s    t    u    v    w    x    y    z
item_6 = ["~", "0", "?", "σ", "2", "5", "7", "μ", "√", "≜", "*", "λ", "%"]

while True:
    print('''
               Encrypt Your Message
            --------------------------
            1. Classical Cryptography
            2. Leet Language
            3. Hash
            4. Quite

            ''')
    command = input("Enter Your Choice: ")
    if command == "1":
        while True:
            print('''
                    Classical Cryptography
                """"""""""""""""""""""""""""""

                      Encrypt your message
                    -------------------------
                    1. Encrypt
                    2. Decrypt
                    3. Back

                    ''')
            command_2 = input("Enter Your Choice: ")
            if command_2 == "1":
                def encrypt_1(sentence):
                    trans = ""
                    for element in sentence:
                        if element in "Aa":
                            trans += item_1[0]
                        elif element in "Bb":
                            trans += item_1[1]
                        elif element in "Cc":
                            trans += item_1[2]
                        elif element in "Dd":
                            trans += item_1[3]
                        elif element in "Ee":
                            trans += item_1[4]
                        elif element in "Ff":
                            trans += item_1[5]
                        elif element in "Gg":
                            trans += item_1[6]
                        elif element in "Hh":
                            trans += item_1[7]
                        elif element in "Ii":
                            trans += item_1[8]
                        elif element in "Jj":
                            trans += item_1[9]
                        elif element in "Kk":
                            trans += item_1[10]
                        elif element in "Ll":
                            trans += item_1[11]
                        elif element in "Mm":
                            trans += item_1[12]
                        elif element in "Nn":
                            trans += item_2[0]
                        elif element in "Oo":
                            trans += item_2[1]
                        elif element in "Pp":
                            trans += item_2[2]
                        elif element in "Qq":
                            trans += item_2[3]
                        elif element in "Rr":
                            trans += item_2[4]
                        elif element in "Ss":
                            trans += item_2[5]
                        elif element in "Tt":
                            trans += item_2[6]
                        elif element in "Uu":
                            trans += item_2[7]
                        elif element in "Vv":
                            trans += item_2[8]
                        elif element in "Ww":
                            trans += item_2[9]
                        elif element in "Xx":
                            trans += item_2[10]
                        elif element in "Yy":
                            trans += item_2[11]
                        elif element in "Zz":
                            trans += item_2[12]
                        elif element in " ":
                            trans += " "
                        else:
                            trans += element
                    return trans


                x = encrypt_1(input("\n\nWhat do you want to Encrypt: "))
                print("\n\n\t\t Result: ", x)
                print("\t\t ________________\n\n")

            elif command_2 == "2":
                def decrypt_1(sentence):
                    trans = ""
                    for element in sentence:
                        if element in item_1[0]:
                            trans += "a"
                        elif element in item_1[1]:
                            trans += "b"
                        elif element in item_1[2]:
                            trans += "c"
                        elif element in item_1[3]:
                            trans += "d"
                        elif element in item_1[4]:
                            trans += "e"
                        elif element in item_1[5]:
                            trans += "f"
                        elif element in item_1[6]:
                            trans += "g"
                        elif element in item_1[7]:
                            trans += "h"
                        elif element in item_1[8]:
                            trans += "i"
                        elif element in item_1[9]:
                            trans += "j"
                        elif element in item_1[10]:
                            trans += "k"
                        elif element in item_1[11]:
                            trans += "l"
                        elif element in item_1[12]:
                            trans += "m"
                        elif element in item_2[0]:
                            trans += "n"
                        elif element in item_2[1]:
                            trans += "o"
                        elif element in item_2[2]:
                            trans += "p"
                        elif element in item_2[3]:
                            trans += "q"
                        elif element in item_2[4]:
                            trans += "r"
                        elif element in item_2[5]:
                            trans += "s"
                        elif element in item_2[6]:
                            trans += "t"
                        elif element in item_2[7]:
                            trans += "u"
                        elif element in item_2[8]:
                            trans += "v"
                        elif element in item_2[9]:
                            trans += "w"
                        elif element in item_2[10]:
                            trans += "x"
                        elif element in item_2[11]:
                            trans += "y"
                        elif element in item_2[12]:
                            trans += "z"
                        elif element in " ":
                            trans += " "
                        else:
                            trans += element
                    return trans


                x = decrypt_1(input("\n\nWhat do you want to Decrypt: "))
                print("\n\n\t\t Result: ", x)
                print("\t\t ________________\n\n")
            elif command_2 == "3":
                print("Thank You!")
                break
            else:
                print("Wrong Input!")

    elif command == "2":
        while True:
            print('''
                          Encrypt Your Message 
                       --------------------------
                       1. Leet Label One
                       2. Leet Label Two 
                       3. Back

                       ''')
            command_3 = input("Enter Your Choice: ")
            if command_3 == "1":
                while True:
                    print('''
                            Leet Language Label One
                        """"""""""""""""""""""""""""""

                             Encrypt your message
                            -----------------------
                            1. Encrypt
                            2. Decrypt
                            3. Back

                            ''')
                    command_4 = input("Enter Your Choice: ")
                    if command_4 == "1":
                        def encrypt(sentence):
                            trans = ""
                            for element in sentence:
                                if element in "Aa":
                                    trans += item_3[0]
                                elif element in "Bb":
                                    trans += item_3[1]
                                elif element in "Cc":
                                    trans += item_3[2]
                                elif element in "Dd":
                                    trans += item_3[3]
                                elif element in "Ee":
                                    trans += item_3[4]
                                elif element in "Ff":
                                    trans += item_3[5]
                                elif element in "Gg":
                                    trans += item_3[6]
                                elif element in "Hh":
                                    trans += item_3[7]
                                elif element in "Ii":
                                    trans += item_3[8]
                                elif element in "Jj":
                                    trans += item_3[9]
                                elif element in "Kk":
                                    trans += item_3[10]
                                elif element in "Ll":
                                    trans += item_3[11]
                                elif element in "Mm":
                                    trans += item_3[12]
                                elif element in "Nn":
                                    trans += item_4[0]
                                elif element in "Oo":
                                    trans += item_4[1]
                                elif element in "Pp":
                                    trans += item_4[2]
                                elif element in "Qq":
                                    trans += item_4[3]
                                elif element in "Rr":
                                    trans += item_4[4]
                                elif element in "Ss":
                                    trans += item_4[5]
                                elif element in "Tt":
                                    trans += item_4[6]
                                elif element in "Uu":
                                    trans += item_4[7]
                                elif element in "Vv":
                                    trans += item_4[8]
                                elif element in "Ww":
                                    trans += item_4[9]
                                elif element in "Xx":
                                    trans += item_4[10]
                                elif element in "Yy":
                                    trans += item_4[11]
                                elif element in "Zz":
                                    trans += item_4[12]
                                elif element in " ":
                                    trans += " "
                                else:
                                    trans += element
                            return trans


                        x = encrypt(input("\n\nWhat do you want to Encrypt: "))
                        print("\n\n\t\t Result: ", x)
                        print("\t\t ________________\n\n")

                    elif command_4 == "2":
                        def decrypt(sentence):
                            trans = ""
                            for element in sentence:
                                if element in item_3[0]:
                                    trans += "a"
                                elif element in item_3[1]:
                                    trans += "b"
                                elif element in item_3[2]:
                                    trans += "c"
                                elif element in item_3[3]:
                                    trans += "d"
                                elif element in item_3[4]:
                                    trans += "e"
                                elif element in item_3[5]:
                                    trans += "f"
                                elif element in item_3[6]:
                                    trans += "g"
                                elif element in item_3[7]:
                                    trans += "h"
                                elif element in item_3[8]:
                                    trans += "i"
                                elif element in item_3[9]:
                                    trans += "j"
                                elif element in item_3[10]:
                                    trans += "k"
                                elif element in item_3[11]:
                                    trans += "l"
                                elif element in item_3[12]:
                                    trans += "m"
                                elif element in item_4[0]:
                                    trans += "n"
                                elif element in item_4[1]:
                                    trans += "o"
                                elif element in item_4[2]:
                                    trans += "p"
                                elif element in item_4[3]:
                                    trans += "q"
                                elif element in item_4[4]:
                                    trans += "r"
                                elif element in item_4[5]:
                                    trans += "s"
                                elif element in item_4[6]:
                                    trans += "t"
                                elif element in item_4[7]:
                                    trans += "u"
                                elif element in item_4[8]:
                                    trans += "v"
                                elif element in item_4[9]:
                                    trans += "w"
                                elif element in item_4[10]:
                                    trans += "x"
                                elif element in item_4[11]:
                                    trans += "y"
                                elif element in item_4[12]:
                                    trans += "z"
                                elif element in " ":
                                    trans += " "
                                else:
                                    trans += element
                            return trans


                        # print("Result: "+decrypt_01(input("\n\nWhat do want to Decrypt: ")))
                        x = decrypt(input("\n\nWhat do you want to Decrypt: "))
                        print("\n\n\t\t Result: ", x)
                        print("\t\t ________________\n\n")
                    elif command_4 == "3":
                        print("Thank You!")
                        break
                    else:
                        print("Wrong Input!")
            if command_3 == "2":
                while True:
                    print('''
                            Leet Language Label Two
                        """"""""""""""""""""""""""""""

                             Encrypt your message
                            -----------------------
                            1. Encrypt
                            2. Decrypt
                            3. Back

                            ''')
                    command_5 = input("Enter Your Choice: ")
                    if command_5 == "1":
                        def encrypt(sentence):
                            trans = ""
                            for element in sentence:
                                if element in "Aa":
                                    trans += item_5[0]
                                elif element in "Bb":
                                    trans += item_5[1]
                                elif element in "Cc":
                                    trans += item_5[2]
                                elif element in "Dd":
                                    trans += item_5[3]
                                elif element in "Ee":
                                    trans += item_5[4]
                                elif element in "Ff":
                                    trans += item_5[5]
                                elif element in "Gg":
                                    trans += item_5[6]
                                elif element in "Hh":
                                    trans += item_5[7]
                                elif element in "Ii":
                                    trans += item_5[8]
                                elif element in "Jj":
                                    trans += item_5[9]
                                elif element in "Kk":
                                    trans += item_5[10]
                                elif element in "Ll":
                                    trans += item_5[11]
                                elif element in "Mm":
                                    trans += item_5[12]
                                elif element in "Nn":
                                    trans += item_6[0]
                                elif element in "Oo":
                                    trans += item_6[1]
                                elif element in "Pp":
                                    trans += item_6[2]
                                elif element in "Qq":
                                    trans += item_6[3]
                                elif element in "Rr":
                                    trans += item_6[4]
                                elif element in "Ss":
                                    trans += item_6[5]
                                elif element in "Tt":
                                    trans += item_6[6]
                                elif element in "Uu":
                                    trans += item_6[7]
                                elif element in "Vv":
                                    trans += item_6[8]
                                elif element in "Ww":
                                    trans += item_6[9]
                                elif element in "Xx":
                                    trans += item_6[10]
                                elif element in "Yy":
                                    trans += item_6[11]
                                elif element in "Zz":
                                    trans += item_6[12]
                                elif element in " ":
                                    trans += " "
                                else:
                                    trans += element
                            return trans


                        x = encrypt(input("\n\nWhat do you want to Encrypt: "))
                        print("\n\n\t\t Result: ", x)
                        print("\t\t ________________\n\n")

                    elif command_5 == "2":
                        def decrypt(sentence):
                            trans = ""
                            for element in sentence:
                                if element in item_5[0]:
                                    trans += "a"
                                elif element in item_5[1]:
                                    trans += "b"
                                elif element in item_5[2]:
                                    trans += "c"
                                elif element in item_5[3]:
                                    trans += "d"
                                elif element in item_5[4]:
                                    trans += "e"
                                elif element in item_5[5]:
                                    trans += "f"
                                elif element in item_5[6]:
                                    trans += "g"
                                elif element in item_5[7]:
                                    trans += "h"
                                elif element in item_5[8]:
                                    trans += "i"
                                elif element in item_5[9]:
                                    trans += "j"
                                elif element in item_5[10]:
                                    trans += "k"
                                elif element in item_5[11]:
                                    trans += "l"
                                elif element in item_5[12]:
                                    trans += "m"
                                elif element in item_6[0]:
                                    trans += "n"
                                elif element in item_6[1]:
                                    trans += "o"
                                elif element in item_6[2]:
                                    trans += "p"
                                elif element in item_6[3]:
                                    trans += "q"
                                elif element in item_6[4]:
                                    trans += "r"
                                elif element in item_6[5]:
                                    trans += "s"
                                elif element in item_6[6]:
                                    trans += "t"
                                elif element in item_6[7]:
                                    trans += "u"
                                elif element in item_6[8]:
                                    trans += "v"
                                elif element in item_6[9]:
                                    trans += "w"
                                elif element in item_6[10]:
                                    trans += "x"
                                elif element in item_6[11]:
                                    trans += "y"
                                elif element in item_6[12]:
                                    trans += "z"
                                elif element in " ":
                                    trans += " "
                                else:
                                    trans += element
                            return trans


                        # print("Result: "+decrypt_01(input("\n\nWhat do want to Decrypt: ")))
                        x = decrypt(input("\n\nWhat do you want to Decrypt: "))
                        print("\n\n\t\t Result: ", x)
                        print("\t\t ________________\n\n")
                    elif command_5 == "3":
                        print("Thank You!")
                        break
                    else:
                        print("Wrong Input!")
            elif command_3 == "3":
                print("Thank You!")
                break
            else:
                print("wrong input")
    elif command == "3":
        while True:
            print('''
                          Hash your Text
                       """"""""""""""""""""
                       1. SHA1
                       2. SHA256 
                       3. SHA386
                       4. SHA512
                       5. Back

                       ''')
            command_6 = input("Enter Your Choice: ")
            if command_6 == "1":
                print('''
                                   SHA1
                             ---------------
                    ''')
                sha_1 = input("Enter Your text: ")
                result = hashlib.sha1(sha_1.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_6 == "2":
                print('''
                                 SHA256
                             ---------------
                    ''')
                sha_256 = input("Enter Your text: ")
                result = hashlib.sha256(sha_256.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_6 == "3":
                print('''
                                 SHA384
                             ---------------
                    ''')
                sha_384 = input("Enter Your text: ")
                result = hashlib.sha384(sha_384.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_6 == "4":
                print('''
                                 SHA512
                             ---------------
                    ''')
                sha_512 = input("Enter Your text: ")
                result = hashlib.sha384(sha_512.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_6 == "5":
                print("Thank You!")
                break
            else:
                print("wrong input")
    elif command == "4":
        print("Thank You!")
        break
    else:
        print("Wrong Input!")

