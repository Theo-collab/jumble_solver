"""
A module that takes a word as a user input and finds its (sub-)anagrams
in a provided word list.
To use:
$ python3 jumble_solver.py word_list.txt hired


Complexity:
1) Assumptions:
- word list consists of n words
- each word has an average of m letters

2) Calculation:
- Looping over the word list in the main function is of O(n) if the
word list consists of n words
- Looping over the letters of a word in the check_sub_anagram_and_print
function is of O(m) if the average word has m letters

-> Both loops are nested which results in O(n*m), where n>>m

Note:
check_sub_anagram_and_print function checks the roughest filter of word
length first and then only compares letters of words that are a subset of
each other. This is like a filter with increasing fineness of granularity.
"""

import sys


def get_word_list() -> list:
    """
    Get words from the CLI word list as a list.
    """
    return open(sys.argv[1]).read().split('\n')


def get_word() -> str:
    """
    Get the word from the CLI as a string.
    """
    return sys.argv[2]


def check_sub_anagram_and_print(word1: str, word2: str):
    """
    Check if word2 is a (sub-)anagram of word1 and prints word2 if it is.

    Args:
    word1 str
    word2 str
    """
    word1_letters: list = sorted(word1)
    word2_letters: list = sorted(word2)
    if len(word1_letters) >= len(word2_letters):  # roughest filter
        if word2 != word1 and set(word2_letters).issubset(set(word1_letters)):
            # A subset can contain several elements of the same kind.
            # Therefore, the following for loop 'crosses out' word2 letters
            # by the letter in word1. When all letters from word1 are checked
            # and word2's letter list is empty: a (sub-)anagram is found and
            # printed.
            for letter in word1_letters:
                try:
                    word2_letters.remove(letter)
                    if not word2_letters:
                        print(word2)
                except ValueError:
                    pass  # No letters left to remove which means no anagrams.


def main():
    """
    Get user inputs of input word and word list from CLI
    and print out (sub-)anagrams of input word in word list.
    """
    word_list = get_word_list()
    input_word = get_word()
    for word in word_list:
        check_sub_anagram_and_print(input_word, word)


if __name__ == '__main__':
    main()
