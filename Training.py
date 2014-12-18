#!/usr/bin/env python

import os
import sys
import re

#IF ELIF AND ELSE PRACTICE
# def maxnumber(a,b,c):
# #    a = [1]
# #    b = [3]
#     if a > b and a > c:
#         print a
#     elif b > a and b > c:
#         print b
#     else:
#         print c
#
# print maxnumber(7,10.1,6)

#FINDING HOW MANY CHARACTERS IN STRING WITHOUT O=USING LEN **STILL WORKING ON**
# def findinglength(word):
#     word = 'helloworld'
#     length = 0
#     for a in word:
#         length = a + length
#
# print findinglength(word)
#
# str = "Mary had a little lamb"
# print str.count("a-z")
# def count_letters(word):
#     count = 0
#     for c in word:
#         if c == "[a-z, A-Z]":
#             count += 1
#     return count
#
# print count_letters("hello")

#TESTING FOR A VOWEL LESSON
# vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# def a_vowel(char):
#     if char in vowel:
#         return True
#     else:
#         return False
#
# print a_vowel('A')

#COMBINING TWO FUNCTIONS TOGETHER #1

# def list_my_word():
#     word = raw_input("Type your word: ").strip()
#     print "You have entered: ", word
#     print
#
#     list_letters(word)
#     a_vowel(word)
#
# #     list_letters('hello')
# #     a_vowel(list_letters('hello'))
# #
# def list_letters(word):
#     for letter in word:
#         print letter
#
# #print list_letters('hello')
#
# vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# def a_vowel(word):
#     for char in word:
#         if char in vowel:
#             print char
#         else:
#             print '*'
#
# #print a_vowel('a')
#
#
# if __name__ == '__main__':
#     list_my_word()

#WRITE A FUNCTION TRANSLATE #5 first attempt

# def translate():
#     #hello world = hohelollolo wowororloldod
#     sentence = raw_input("Type your word: ").strip()
#     print "You have entered: ", sentence
#     print
#
#     adding_o(sentence)
#
# vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# def adding_o(sentence):
# #    print sentence
# #     for word in sentence:
#     split_words = sentence.split(" ")
#     print split_words

#first way trying ******
#     for word in split_words:
# #        print word
#
#         for char in word:
# #            print char
#
#             if char not in vowel:
#                 char += str('o'+char)
#                 return [str(char)]
#             else:
#                 return [char]
#     print word

#second way trying *******



#joining characters back together
    # str = ''
    # for letter in a:
    #     str += letter
    # print str
#another way to join string..
    #     a = ['char']
    # ''.join(char)
#
#
# if __name__ == '__main__':
#     translate()

    #WRITE A FUNCTION TRANSLATE #5 second attempt

def translate(sentence):
    #hello world = hohelollolo wowororloldod
    sentence = raw_input("Type your word: ").strip()
#    print "You have entered: ", sentence
#    print

    consonants = 'bcdfghjklmnpqrstvwxyz'
    return ''.join(l + 'o' + l if l in consonants else l for l in sentence)

print (translate("hello world"))