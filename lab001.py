# ----------------------------- Take input from user and print table -----------------------------

# user_input = int(input("Enter the number: "))
#
# def print_table(inp):
#     for i in range(1, 11):
#         print(f'{inp}*{i} =', inp * i)
#
# print_table(int(input("Enter the number: ")))

# ================

# def generate_grade(marks):
#     if marks >= 90 and marks <= 100:
#         grade = 'A'
#     elif marks >= 80 and marks <= 89:
#         grade = 'B'
#     elif marks >= 70 and marks <= 79:
#         grade = 'C'
#     elif marks >= 60 | marks <= 69:
#         grade = 'D'
#     else:
#         grade = 'F'
#     return grade

# marks = 90
# result = generate_grade(marks)
# print(f"Based on your {marks} marks, your grade is {result}")
#
# # Find the maximum of 3 numbers using ternary operator
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
# max_value = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
# print(f"The maximum of {num1}, {num2}, {num3} is: {max_value}")


# ----------------------------- Find the average of N numbers -----------------------------

# n = int(input("Enter the number: "))
# num = 0
# def find_average(inp):
#     global num
#     for i in range(1, inp + 1):
#         num += 1
#     avg = num / inp
#     return avg
#
# res = find_average(n)
# print(f"The average of the first {n} positive integers is: {res}")

# ----------------------------- How to sum the first N positive integers in Python -----------------------------

# num_inputs = int(input("Enter the number of inputs: "))
# def generate_inputs(n):
#     inputs = []
#     for i in range(0, n):
#         inp = int(input(f"Enter the input {i + 1}: "))
#         inputs.append(inp)
#
#     return inputs
#
# # calculating sum of positive numbers
# def calculate_sum_of_first_positive_num(input):
#     num_positive = 0
#     for j in input:
#         if j > 0:
#             num_positive += j
#     return num_positive
#
# generated_input = generate_inputs(num_inputs)
# print("Generated inputs are: ", generated_input)
#
# sum_of_positive = calculate_sum_of_first_positive_num(generated_input)
# print("Sum of positive numbers is: ", sum_of_positive)
#

# --------------------------- Factorial -------------------------
# user_input = int(input("Enter the number: "))
# def find_factorial(num):
#     temp = 0
#     if num < 0:
#         print("Factorial not possible")
#     else:
#         for i in range(1, num + 1):
#             temp += i
#         return temp
#
# res = find_factorial(user_input)
# print("Result is: ", res)

# ========================= Basic List Programs ==================================

# ------------------ Reversing a List ------------------
# my_list = [2, 4, 5, 3, 7, 6]
# def reverse_the_list(inp):
#     temp_list = []
#     for i in range(len(inp)):
#         temp_list.insert(0, inp[i])
#     print("New reversed list: ", temp_list)
#
# reverse_the_list(my_list)

# ------------------- Cloning or Copying a list -------------------
# my_list_01 = [1, 2, 3, 4, 5, 6]
# def clone_list(li01):
#     my_list_02 = []
#     my_list_02.extend(my_list_01)
#     return my_list_02
# res = clone_list(my_list_01)
# print("Copied list", res)

# -------------------- Count occurrences of an element in a list -------------------
# my_list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# elem = 7
# count = 0
#
# def count_occurrences_of_element(el):
#     global count
#     for el in my_list:
#         if el == elem:
#             count += 1
#         else:
#             continue
#     return count
#
# res = count_occurrences_of_element(my_list)
# print(f"Count of {elem} is: ", res)

# --------------------- Remove empty List from List --------------------
# test_list = [5, 6, [], 3, [], [], 9]
# def remove_empty_list(li):
#     copy_li = []
#     for i in li:
#         if i:
#             copy_li.append(i)
#     return copy_li
# res = remove_empty_list(test_list)
# print(res)

# ------------- Remove empty tuples from a list ----------------
# test_list = [(), ("ram", "15", "8"), (), ("laxman", "sita"), ("krishna", "akbar", "45"), ("", ""), ()]
#
# def remove_empty_tuple(inp_list):
#     copy_list = []
#     for list_elem in inp_list:
#         if list_elem and list_elem[0] != "":
#             copy_list.append(list_elem)
#     print("Each list elem :", copy_list)
# remove_empty_tuple(test_list)

# ------------- Program to print duplicates from a list of integers ------------------
# my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# def print_remove_duplicates(li):
#     unique = []
#     for item in li:
#         if item not in unique:
#             unique.append(item)
#     print(unique)
# print_remove_duplicates(my_list)

# Uncommon elements in Lists of List
# test_list1 = [ [1, 2], [3, 4], [5, 6] ]
# test_list2 = [ [3, 4], [5, 7], [1, 2] ]
#
# def remove_uncommon_elements(li_01, li_02):
#     uncommon_list = []
#     for i in li_01:
#         if i not in li_02:
#             uncommon_list.append(i)
#     for j in li_02:
#         if j not in li_01:
#             uncommon_list.append(j)
#     print(uncommon_list)
# remove_uncommon_elements(test_list1, test_list2)

# Reverse Row sort in Lists of List
# The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
# The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]