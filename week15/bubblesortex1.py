def bubble_sort(list_to_sort):
	
  for outer_index in range(0, len(list_to_sort) - 1):
    
    has_made_changes = False
	

    for index in range(0, len(list_to_sort) - 1 - outer_index):
      
      current_element = list_to_sort[index]
      next_element = list_to_sort[index + 1]

      print(f'-- Iteration {outer_index}, {index}. Current Element: {current_element}, Next Element: {next_element}')


      if current_element > next_element:
        print('The current element is greater than the next. Swapping them...')
        list_to_sort[index] = next_element
        list_to_sort[index + 1] = current_element
        has_made_changes = True


    if not has_made_changes:
      return


my_test_list = [7, 52, 31, 10, 14, 25, 64, 37, 81]
bubble_sort(my_test_list)

print(my_test_list)