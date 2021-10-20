# jumble_solver
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
