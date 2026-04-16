def print_words_by_length(filename,length):
    file = open("SANGEETA.txt","r")
    text = file.read()
    file.close()
    words = text.split()
    print(f"words of length {length}:")
    for word in words:
        if len(word)==length:
            print(word)

fname = input("enter file name:")
l = int(input("enter a word length:"))
print_words_by_length(fname,1)
