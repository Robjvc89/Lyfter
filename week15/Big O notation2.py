def print_numbers_times_2(numbers_list):
	for number in numbers_list:            #O(n) where n is the number of elements in the list.
		print(number * 2)                  #O(1) This is constant time operation.
		


def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:              #O(n) where n is the number of elements in the list.
		for element_b in list_b:          #O(n) where n is the number of elements in the list.
			if element_a == element_b:    #O(1) because comparing two elements is done in constant time.
				return True               #O(1) it may terminate early when a match is found.
				
	return False                          #O(1)  it only occurs at the end of the function.



def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)           #O(1) This is constant time operation.
	for index in range(min(list_len, 10)):  #O(1) because the number of iterations is capped at a constant value.
		print(list_to_print[index])         #O(1), because it simply prints an element.
		


def generate_list_trios(list_a, list_b, list_c):
	result_list = []                       #O(1) This is constant time operation.
	for element_a in list_a:               #O(n) where n is the number of elements in the list.
		for element_b in list_b:           #O(n) where n is the number of elements in the list.
			for element_c in list_c:       #O(n) where n is the number of elements in the list.
				result_list.append(f'{element_a} {element_b} {element_c}')  #O(1), as appending to a list is a constant-time operation.
				
	return result_list                     #O(1) This is constant time operation.