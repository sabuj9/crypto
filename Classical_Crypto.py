# a to m|  1   2     3    4    5    6    7    8    9   10    11   12   13
item_1 = ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# n to z| 14   15   16   17   18   19   20   21   22   23    24   25   26
item_2 = ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"]

while True:
    print('''
            Classical Cryptography
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


        x = encrypt(input("\n\nWhat do want to Encrypt: "))
        print("\n\n\t\t Result: ", x)
        print("\t\t ________________\n\n")

    elif command == "2":
        def decrypt(sentence):
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


        # print("Result: "+decrypt_01(input("\n\nWhat do want to Decrypt: ")))
        x = decrypt(input("\n\nWhat do want to Decrypt: "))
        print("\n\n\t\t Result: ", x)
        print("\t\t ________________\n\n")
    elif command == "3":
        print("Thank You!")
        break
    else:
        print("Wrong Input!")
