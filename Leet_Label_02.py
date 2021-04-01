# (a to m) a    b    c    d    e    f    g    h    i    j    k    l    m
item_5 = ["4", "8", "(", "δ", "3", "}", "9", "#", "!", "]", "X", "1", "ψ"]

# (n to z) n    o    p    q    r    s    t    u    v    w    x   y    z
item_6 = ["~", "0", "?", "σ", "2", "5", "7", "μ", "√", "≜", "*", "λ", "%"]

while True:
    print('''
            Leet Language Label Two
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


        x = encrypt(input("\n\nWhat do want to Encrypt: "))
        print("\n\n\t\t Result: ", x)
        print("\t\t ________________\n\n")

    elif command == "2":
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
        x = decrypt(input("\n\nWhat do want to Decrypt: "))
        print("\n\n\t\t Result: ", x)
        print("\t\t ________________\n\n")
    elif command == "3":
        print("Thank You!")
        break
    else:
        print("Wrong Input!")
