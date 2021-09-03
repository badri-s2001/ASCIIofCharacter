while True:
    a = input("Enter a character: ")
    if type(a) != 'str' and len(a) != 1:
        print("Please enter character only")
    else:
        print(ord(a))
        break
