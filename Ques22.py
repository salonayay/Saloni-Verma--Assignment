def find_min_max(input_list):
    if len(input_list) == 0:
        return None, None
    
    min_value = min(input_list)
    max_value = max(input_list)
    
    return min_value, max_value

# Test the function
numbers = [1, 2, 3, 4, 5]
min_value, max_value = find_min_max(numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)