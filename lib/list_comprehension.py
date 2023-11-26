#!/usr/bin/env python3

#  USING A LIST COMPREHENSION
def return_evens(num_list):
    even_numbers = [item for item in num_list if item % 2 ==0 ]
    return even_numbers

print(return_evens([1,2,3,4,5,6,7,8,32,45,67,88]))

#    USING FOR LOOP
# def return_evens(num_list):
#     even_numbers  = list()
#     for item in num_list:
#         if item % 2 == 0 :
#             even_numbers.append(item)
#     return even_numbers


#  USING A LIST COMPREHENSION
def make_exclamation(sentence_list):
    new_sentence_list = [item + "!" for item in sentence_list]
    return new_sentence_list

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

#    USING FOR LOOP
# def make_exclamation(sentence_list):
#     new_sentence_list = list()
#     for item in sentence_list:
#         new_sentence_list.append(item + "!")
#     return new_sentence_list

