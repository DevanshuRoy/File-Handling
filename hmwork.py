print("What would you like to do?")
print("1) Find number of words")
print("2) Count number of words starting with t")

choice=int(input("Enter your choice (1 or 2): "))

if choice==1:
    file=open("Generated.txt")
    print("reading data...")
    ch=file.read(1)
    wordcount=0
    in_word=False

    while ch:
        if ch == " " or ch == "\n":
            wordcount+=1
            in_word=False
        else:
            in_word=True
        ch=file.read(1)

    if in_word:
        wordcount+=1

    print("Number of words in the file:", wordcount)

elif choice==2:
    file=open("Generated.txt")
    print("reading data...")
    ch=file.read(1)
    wordcount=0

    while ch:
        if ch == " ":
            next_char = file.read(1)
            if next_char.lower() == "t" or next_char == "t":
                wordcount+=1
        ch=file.read(1)

    print("Number of words starting with 't':", wordcount)

else:
    print("Invalid choice. Please enter 1 or 2.")