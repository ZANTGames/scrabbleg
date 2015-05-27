from hand import *

WORDLIST_FILENAME = "words.txt"

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def load_words():

    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist


def get_frequency_dict(sequence):

    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word, n):

    word = word.lower()
    score = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]

    if len(word) == n:
        score += 50

    return score


def is_valid_word(word, hand, word_list):

    if word in word_list:
        for letter in word:
            if letter in hand:
                hand = update_hand(hand, word)
                if hand == False:
                    return ('False', hand)
                else:
                    # print 'this'
                    return ('True', hand)
            else:

                return ('False', hand)
    else:
        return ('False', hand)
