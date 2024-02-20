'''
# Python Program to count unique values inside a list
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

def count_unique_values(li):
    temp_list = []
    count = 0
    for el in li:
        if el not in temp_list:
            temp_list.append(el)
            count +=1
    return count

res = count_unique_values(input_list)
print(res)

# ===========================================================

# Python – Extract elements with Frequency greater than K

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3

def extract_element_greater_than_k(test_list):
    extracted_elements_list = []
    count = 1
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list)):
            if test_list[i] == test_list[j]:
                count += 1
                if count > K:
                    count = 1
                    extracted_elements_list.append(test_list[j])

    return extracted_elements_list

extract_element_greater_than_k(test_list)

'''


# Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4]

'''
def capital_indexes(inp):
    res = []
    for elem in range(len(inp)):
        if(inp[elem].isupper()):
            res.append(elem)
    return res

op = capital_indexes("HeLlO")
print(op)

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter.
# If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return ""

def mid(inp):
    if(len(inp) % 2 == 0):
        print("String does not contain middle letter")
    else:
        print(int(len(inp) // 2))
mid("Sahil")

# Write a function named online_count that takes one parameter.
# The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
def online_count(inp):
    count_ = 0
    for elem in dict.values(inp):
        if(elem == "online"):
            count_+=1
    return count_

print(online_count(statuses))

# Define a function, random_number, that takes no parameters. 
# The function must generate a random integer between 1 and 100, both inclusive, and return it.
# Calling the function multiple times should (usually) return different numbers.

import random
def random_number():
    return random.randint(1,100)

print(random_number())

# check if it contains two of the same letter in a row.
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

def double_letters(inp):
    for elem in range(len(inp)-1):
        # print(elem+1)
        if inp[elem] == inp[elem+1]:
            return True
        else:
            continue
    return False

print(double_letters("nono"))


# Write a function named add_dots that takes a string and adds "." in between each letter.
# For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string.
# For example, calling remove_dots("t.e.s.t") should return "test".

def add_dots(inp):
    return ".".join(inp)

def remove_dots(inp):
    res = inp.split(".")
    return "".join(res)

print(add_dots("test"))
print(remove_dots("test"))


# Define a function named count that takes a single parameter. The parameter is a string.
# The string will contain a single word divided into syllables by hyphens, such as these:
ex:
"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"

def count(inp):
    count = 0
    temp = inp.split("-")
    for el in temp:
        if el != "-":
            count += 1
    return count


print(count("ter-min-a-tor"))
'''

# Write a function named is_anagram that takes two strings as its parameters.
# Your function should return True if the strings are anagrams, and False otherwise.

def check_anagram(str_01, str_02):
    dict_01 = {}
    dict_02 = {}
    for i in str_01:    # for dict 01
        if i in dict_01:
            dict_01[i] += 1
        else:
           dict_01[i] = 1

    for j in str_02:
        if j in dict_02:
            dict_02[j] += 1
        else:
            dict_02[j] = 1
    print(dict_01 == dict_02)

check_anagram("secure", "rescue")





















