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
'''
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
