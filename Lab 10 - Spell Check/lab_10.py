import re

def split_line(line):
    """ Split a line of text into words and return a list of words. """
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

def read_dictionary(file_path):
    dictionary_list = []
    with open(file_path, 'r') as file:
        for line in file:
            dictionary_list.append(line.strip().upper())
    return dictionary_list

def linear_search(dictionary_list, word):
    """ Perform a linear search for the word in the dictionary list. """
    for dict_word in dictionary_list:
        if dict_word == word:
            return True
    return False

def binary_search(dictionary_list, word):
    """ Perform a binary search for the word in the dictionary list. """
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
    dictionary_list = read_dictionary('dictionary.txt')
    line_number = 0

    print("--- Linear Search ---")
    with open('AliceInWonderLand200.txt', 'r') as file:
        for line in file:
            line_number += 1
            word_list = split_line(line)
            for word in word_list:
                if not linear_search(dictionary_list, word.upper()):
                    print(f"Line {line_number} possible misspelled word: {word}")

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
