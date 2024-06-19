def count_occurrences(input_list, element):
    return input_list.count(element)

# Test the function
my_list = [1, 2, 3, 4, 2, 2, 5, 6]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list")