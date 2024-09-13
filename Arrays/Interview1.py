"""
Take a nested list and return a single flattened list with all values except nil/null.

The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

For Example

input: [1,[2,3,null,4],[null],5]
"""

def flatten(lst):
    flattened_list = []
    
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        elif item is not None:  # Ignore None (equivalent of null in Python)
            flattened_list.append(item)
    
    return flattened_list

# Example usage:
input_list = [1, [2, 3, None, 4], [None], 5]
output = flatten(input_list)
print(output)  # Output: [1, 2, 3, 4, 5]


