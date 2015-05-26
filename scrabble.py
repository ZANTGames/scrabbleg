
import random
import string, os

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

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
        freq[x] = freq.get(x,0) + 1
    return freq


def get_word_score(word, n):
    
    word = word.lower()
    score = 0
    for letter in word:
        score = score + SCRABBLE_LETTER_VALUES[letter]

    if len(word) == n:
        score += 50

    return score

def display_hand(hand):
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

def deal_hand(n):
    
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def update_hand(hand, word):
    
    for letter in word:
        if hand[letter] > 0:
            hand[letter] = hand[letter] - 1
        else:
            return False

    return hand

def is_valid_word(word, hand, word_list):
   
    if word in word_list:
        for letter in word:
            if letter in hand:
                hand = update_hand(hand, word)
                if hand == False:
                    return ('False', hand) 
                else:
                    #print 'this'
                    return ('True', hand)  
            else:

                return ('False', hand)
    else:
        return ('False', hand)

def play_hand(hand, word_list):
    
    display_hand(hand)
    
    score = 0
    
    while 1:
        word = raw_input("Input a word from your hand : ")
        if word == '.':
            print 'Not Playing this hand.'
            print 'Final Score remians :', score
            break
    
        (valid, temp) = is_valid_word(word, hand, word_list)
        #print valid, hand
    
        if valid == 'True':
            print 'Word Accepted'
            hand = temp
            score += get_word_score(word, n)
            print 'Your new score :', score
            break
        else:
            print 'Sorry, the word you entered is either invalid or not from your hand.'

def play_game(word_list):
    
    print 'Input a value out of these :'
    print 'n >> Play a new hand'
    print 'e >> Exit'
    play = 0
    while 1:
        value = raw_input('Input : ')
        if value == 'n':
            prev_hand = deal_hand(HAND_SIZE)
            play_hand(prev_hand.copy(), word_list)
            play = 1
        elif value == 'r' and play!=0:
            play_hand(prev_hand.copy(), word_list)
        elif value == 'e':
            print 'Thank You for trying out this game !'
            print 'Bye-Bye'
            break
        else:
            print 'Invalid Input'
        print 'Input a value out of these :'
        print 'n >> Play a new hand'
        print 'r >> Replay the last hand'
        print 'e >> Exit'

if __name__ == '__main__':
    os.system('clear')
    word_list = load_words()
    play_game(word_list)

