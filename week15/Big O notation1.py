def bubble_sort(list_to_sort):
	
  for outer_index in range(0, len(list_to_sort) - 1):    #O(n), where n is the length of the list.
    
    has_made_changes = False   #O(1), this is a constant time operation.
	

    for index in range(0, len(list_to_sort) - 1 - outer_index):  #O(n2)in the worst case, it runs n - 1, n - 2, ..., 1 times.
      
      current_element = list_to_sort[index]      #O(1) These are constant time operations
      next_element = list_to_sort[index + 1]     #O(1) These are constant time operations

      print(f'-- Iteration {outer_index}, {index}. Current Element: {current_element}, Next Element: {next_element}')
            #O(1) This line prints the current elements being compared, which doesn't affect the time complexity

      if current_element > next_element:    # O(1) because it's a simple comparison.
        print('The current element is greater than the next. Swapping them...')   #O(1) These are constant time operations
        list_to_sort[index] = next_element             #O(1) These are constant time operations    
        list_to_sort[index + 1] = current_element      #O(1) These are constant time operations
        has_made_changes = True                        #O(1) These are constant time operations


    if not has_made_changes:      #O(1), as it's a simple check.
      return                      #O(1), this line ends the function early if the list is already sorted


my_test_list = [7, 52, 31, 10, 14, 25, 64, 37, 81]    #O(1) These are constant time operations  
bubble_sort(my_test_list)                             #O(1) These are constant time operations  

print(my_test_list)                                   #O(1) These are constant time operations  
