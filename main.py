def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}
    lower = text.lower()
    for letter in lower:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


def report_letters(text):
    letters = count_letters(text)
    letterlist = list(letters.items())
    letterlist.sort()
    for letter in letterlist:
        if letter[0].isalpha():
            print(f"The {letter[0]} character was found {letter[1]} times")


filename = "books/frankenstein.txt"
with open(filename) as f:
    file_contents = f.read()
print(f"--- Begin report of {filename} ---")
report_letters(file_contents)
print("--- End report ---")
