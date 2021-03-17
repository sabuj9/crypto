# a to m|  1   2     3    4    5    6    7    8    9   10    11   12   13
item_3 = ["4", "8", "c", "d", "3", "f", "9", "h", "1", "j", "k", "l", "m"]
# n to z| 14   15   16   17   18   19   20   21   22   23    24   25   26
item_4 = ["n", "0", "p", "q", "2", "5", "7", "u", "v", "w", "x", "y", "z"]


while True:
    print('''
            Leet Language Label One
        """"""""""""""""""""""""""""""
        
            Encrypt your message
            --------------------
            1. Encrypt
            2. Decrypt
            3. Quit

            ''')
    command = input("Enter Your Choice: ")
    if command == "1":
        def encrypt(sentence):
            trans = ""
            for element in sentence:
                if element in "Aa":
                    trans = trans + item_3[0]
                elif element in "Bb":
                    trans = trans + item_3[1]
                elif element in "Cc":
                    trans = trans + item_3[2]
                elif element in "Dd":
                    trans = trans + item_3[3]
                elif element in "Ee":
                    trans = trans + item_3[4]
                elif element in "Ff":
                    trans = trans + item_3[5]
                elif element in "Gg":
                    trans = trans + item_3[6]
                elif element in "Hh":
                    trans = trans + item_3[7]
                elif element in "Ii":
                    trans = trans + item_3[8]
                elif element in "Jj":
                    trans = trans + item_3[9]
                elif element in "Kk":
                    trans = trans + item_3[10]
                elif element in "Ll":
                    trans = trans + item_3[11]
                elif element in "Mm":
                    trans = trans + item_3[12]
                elif element in "Nn":
                    trans = trans + item_4[0]
                elif element in "Oo":
                    trans = trans + item_4[1]
                elif element in "Pp":
                    trans = trans + item_4[2]
                elif element in "Qq":
                    trans = trans + item_4[3]
                elif element in "Rr":
                    trans = trans + item_4[4]
                elif element in "Ss":
                    trans = trans + item_4[5]
                elif element in "Tt":
                    trans = trans + item_4[6]
                elif element in "Uu":
                    trans = trans + item_4[7]
                elif element in "Vv":
                    trans = trans + item_4[8]
                elif element in "Ww":
                    trans = trans + item_4[9]
                elif element in "Xx":
                    trans = trans + item_4[10]
                elif element in "Yy":
                    trans = trans + item_4[11]
                elif element in "Zz":
                    trans = trans + item_4[12]
                elif element in " ":
                    trans = trans + " "
                else:
                    trans = trans + element
            return trans


        x = encrypt(input("\n\nWhat do want to Encrypt: "))
        print("\n\n\t\t Result: ", x)
        print("\t\t ________________\n\n")

    elif command == "2":
        def decrypt(sentence):
            trans = ""
            for element in sentence:
                if element in item_3[0]:
                    trans = trans + "a"
                elif element in item_3[1]:
                    trans = trans + "b"
                elif element in item_3[2]:
                    trans = trans + "c"
                elif element in item_3[3]:
                    trans = trans + "d"
                elif element in item_3[4]:
                    trans = trans + "e"
                elif element in item_3[5]:
                    trans = trans + "f"
                elif element in item_3[6]:
                    trans = trans + "g"
                elif element in item_3[7]:
                    trans = trans + "h"
                elif element in item_3[8]:
                    trans = trans + "i"
                elif element in item_3[9]:
                    trans = trans + "j"
                elif element in item_3[10]:
                    trans = trans + "k"
                elif element in item_3[11]:
                    trans = trans + "l"
                elif element in item_3[12]:
                    trans = trans + "m"
                elif element in item_4[0]:
                    trans = trans + "n"
                elif element in item_4[1]:
                    trans = trans + "o"
                elif element in item_4[2]:
                    trans = trans + "p"
                elif element in item_4[3]:
                    trans = trans + "q"
                elif element in item_4[4]:
                    trans = trans + "r"
                elif element in item_4[5]:
                    trans = trans + "s"
                elif element in item_4[6]:
                    trans = trans + "t"
                elif element in item_4[7]:
                    trans = trans + "u"
                elif element in item_4[8]:
                    trans = trans + "v"
                elif element in item_4[9]:
                    trans = trans + "w"
                elif element in item_4[10]:
                    trans = trans + "x"
                elif element in item_4[11]:
                    trans = trans + "y"
                elif element in item_4[12]:
                    trans = trans + "z"
                elif element in " ":
                    trans = trans + " "
                else:
                    trans = trans + element
            return trans


        # print("Result: "+decrypt_01(input("\n\nWhat do want to Decrypt: ")))
        x = decrypt(input("\n\nWhat do want to Decrypt: "))
        print("\n\n\t\t Result: ", x)
        print("\t\t ________________\n\n")
    elif command == "3":
        print("Thank You!")
        break
    else:
        print("Wrong Input!")
