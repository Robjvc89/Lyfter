def bubble_sort_reverse(list_to_sort):
    
    for outer_index in range(0, len(list_to_sort) - 1):
        
        has_made_changes = False
        
        # Cambiar la dirección de la comparación para ordenar de derecha a izquierda
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            
            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]
            
            print(f'-- Iteration {outer_index}, {index}. Current Element: {current_element}, Previous Element: {previous_element}')
            
            if current_element < previous_element:
                print('The current element is smaller than the previous. Swapping them...')
                list_to_sort[index] = previous_element
                list_to_sort[index - 1] = current_element
                has_made_changes = True

        
        if not has_made_changes:
            return


my_test_list = [7, 52, 31, 10, 14, 25, 64, 37, 81]
bubble_sort_reverse(my_test_list)

print(my_test_list)
