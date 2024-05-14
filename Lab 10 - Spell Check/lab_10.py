import re


def split_line(line):
    """
    Split a line of text into words using regular expressions and return a list of words.
    Handles standard words and words with apostrophes (e.g., "Alice's").
    """
    return re.findall(r'[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def read_dictionary(file_path):
    """
    Read words from a dictionary file and store them in a list in uppercase.
    """
    dictionary_list = []
    with open(file_path, 'r') as file:
        for line in file:
            dictionary_list.append(line.strip().upper())
    return dictionary_list


def linear_search(dictionary_list, word):
    """
    Perform a linear search for the word in the dictionary list.
    Returns the index of the word if found, or -1 if not found.
    """
    for index, dict_word in enumerate(dictionary_list):
        if dict_word == word:
            return index
    return -1


def binary_search(dictionary_list, word):
    """
    Perform a binary search for the word in the dictionary list.
    Returns True if found, False otherwise.
    """
    low = 0
    high = len(dictionary_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if dictionary_list[mid] < word:
            low = mid + 1
        elif dictionary_list[mid] > word:
            high = mid - 1
        else:
            return True
    return False


def spell_check():
    """
    Perform a spell check using both linear and binary search methods on a text file.
    Compares each word against a dictionary to find possible misspellings.
    """
    dictionary_list = read_dictionary('dictionary.txt')

    # Linear Search Check
    print("--- Linear Search ---")
    line_number = 0
    with open('AliceInWonderLand200.txt', 'r') as file:
        for line in file:
            line_number += 1
            word_list = split_line(line)
            for word in word_list:
                if linear_search(dictionary_list, word.upper()) == -1:
                    print(f"Line {line_number} possible misspelled word: {word}")

    # Binary Search Check
    print("--- Binary Search ---")
    line_number = 0
    with open('AliceInWonderLand200.txt', 'r') as file:
        for line in file:
            line_number += 1
            word_list = split_line(line)
            for word in word_list:
                if not binary_search(dictionary_list, word.upper()):
                    print(f"Line {line_number} possible misspelled word: {word}")


if __name__ == "__main__":
    spell_check()
