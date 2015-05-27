import time
import random
import string
import os
from hand import *
from word import *

def play_hand(hand, word_list):

    display_hand(hand)

    score = 0

    while 1:
        start_time = time.time()
        word = raw_input("Input a word : ")
        
        
        if word == '.':
            print 'Not Playing this hand.'
            end_time = time.time()
            total_time = end_time - start_time
            print 'Time taken to enter : %0.2f' % total_time
            print 'Final Score :', score
            break

        (valid, temp) = is_valid_word(word, hand, word_list)
        # print valid, hand

        if valid == 'True':
            print 'Word Accepted'
            hand = temp
            score += get_word_score(word, HAND_SIZE)
            end_time = time.time()
            total_time = end_time - start_time
            print 'Time taken to enter : %0.2f seconds' % total_time
            print 'Final Score :', score
            break
        else:
            print 'Sorry, the word you entered is either invalid or not from your hand.'


def play_game(word_list):

    print 'Here are the word scores : '
    print SCRABBLE_LETTER_VALUES

    print 'Input a value out of these :'
    print 'n >> Play a new hand'
    print 'e >> Exit'
    play = 0
    while 1:
        value = raw_input('Input : ')
        os.system('clear')
        if value == 'n':
            print 'Initialising hand ... hand size is kept 7'
            prev_hand = deal_hand(HAND_SIZE)
            play_hand(prev_hand.copy(), word_list)
            play = 1
        elif value == 'r' and play != 0:
            play_hand(prev_hand.copy(), word_list)
        elif value == 'e':
            print 'Thank You for trying out this game !'
            print 'Bye-Bye'
            break
        else:
            print 'Invalid Input'
        #os.system('clear')
        print 'Here are the word scores : '
        print SCRABBLE_LETTER_VALUES
        print 'Input a value out of these :'
        print 'n >> Play a new hand'
        print 'r >> Replay the last hand'
        print 'e >> Exit'

if __name__ == '__main__':
    os.system('clear')
    word_list = load_words()
    play_game(word_list)
