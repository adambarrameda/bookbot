def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    report(text, path)
    
def get_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    letter_count = {}
    for char in text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def report(text, filepath):
    word_count = count_words(text)
    letter_count = count_letters(text)
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Begin report of {filepath} ---")
    print(f"Document contains {word_count} words.")
    for char in sorted_letters:
        if char[0].isalpha():
            print(f"The '{char[0]}' character appears {char[1]} times.")
    print("--- End Report ---")

main()