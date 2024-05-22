#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [x for x in num_list if x % 2 == 0]
    print(even_numbers)
    return even_numbers

def make_exclamation(sentence_list):
    new_list = [x + "!" for x in sentence_list]
    print(new_list)
    return new_list