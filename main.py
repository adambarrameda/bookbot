with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)
    words = file_contents.split()
    num_words = len(words)
    print(num_words)