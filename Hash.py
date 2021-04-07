import hashlib

while True:
    print('''
               Encrypt your message
            --------------------------
            1. Hash
            2. Quite

            ''')
    command = input("Enter Your Choice: ")
    if command == "1":
        while True:
            print('''
                          Hash your Text
                       ----------------------
                       1. SHA1
                       2. SHA256 
                       3. SHA386
                       4. SHA512
                       5. Back

                       ''')
            command_2 = input("Enter Your Choice: ")
            if command_2 == "1":
                print('''
                                 SHA1
                             ---------------
                    ''')
                sha_1 = input("Enter Your text: ")
                result = hashlib.sha1(sha_1.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_2 == "2":
                print('''
                                 SHA256
                             ---------------
                    ''')
                sha_256 = input("Enter Your text: ")
                result = hashlib.sha256(sha_256.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_2 == "3":
                print('''
                                SHA384
                             ---------------
                    ''')
                sha_384 = input("Enter Your text: ")
                result = hashlib.sha384(sha_384.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_2 == "4":
                print('''
                                SHA512
                             ---------------
                    ''')
                sha_512 = input("Enter Your text: ")
                result = hashlib.sha384(sha_512.encode())
                print("The hexadecimal equivalent of SHA256 is : ")
                print(result.hexdigest())
            elif command_2 == "5":
                print("Thank You!")
                break
            else:
                print("wrong input")

    elif command == "2":
        print("Thank You!")
        break
    else:
        print("Wrong Input!")
