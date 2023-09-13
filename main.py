# Time to Read the Book def main():
def main():
    path = "books/frank.txt"
    text = get_text(path)
    num_words = word_count(text)
    char_dict = count_letters(text)
    print_report(path, num_words, char_dict)


def get_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def count_letters(text):
    char_dict = {}
    for c in text:
        key = c.lower()
        if key not in char_dict:
            char_dict[key] = 1
        else:
            char_dict[key] += 1
    return char_dict


def print_report(path, num_words, char_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    ls = []
    for k, v in char_dict.items():
        if k.isalpha():
            ls.append((k, v))
    ls.sort(key=lambda x: x[1], reverse=True)
    for x in ls:
        print(f"The '{x[0]}' character was found {x[1]} times")
    print("--- End Report ---")


main()
