
# Menu Driven Program to Convert Text to Various Number Systems
# Includes options to edit the text without stopping or exiting the program
text = input("ENTER ANY TEXT: ")

while True:
    print("\n MENU")
    print("1. CONVERT TO DECIMAL (ASCII)")
    print("2. CONVERT TO BINARY")
    print("3. CONVERT TO OCTAL")
    print("4. CONVERT TO HEXADECIMAL")
    print("5. CONVERT TO ALL")
    print("6. EDIT THE TEXT")
    print("7. EXIT")

    choice = input("ENTER YOUR CHOICE (1-7): ")
    
    if choice == "1":
        print("\nCHARACTER : DECIMAL")
        for ch in text:
            print(f"{ch} : {ord(ch)}")
            
    elif choice == "2":
        print("\nCHARACTER : BINARY")
        for ch in text:
            print(f"{ch} : {bin(ord(ch))[2:]}")
            
    elif choice == "3":
        print("\nCHARACTER : OCTAL")
        for ch in text:
            print(f"{ch} : {oct(ord(ch))[2:]}")

    elif choice == "4":
        print("\nCHARACTER : HEXADECIMAL")
        for ch in text:
            print(f"{ch} : {hex(ord(ch))[2:]}")

    elif choice == "5":
        print("\nCHARACTER | DECIMAL |  BINARY  | OCTAL | HEXADECIMAL")
        print('-' * 55)
        for ch in text:
            d = ord(ch)
            print(f"    {ch}         {d}      {bin(d)[2:]}     {oct(d)[2:]}        {hex(d)[2:].upper()}")
            
    elif choice == "6":
        text = input("\nENTER NEW TEXT: ")
        print("TEXT UPDATED SUCCESSFULLY.")
    
    elif choice == "7":
        print("EXITING THE PROGRAM. GOODBYE!")
        break

    else:
        print("INVALID CHOICE. PLEASE ENTER BETWEEN(1-7).")