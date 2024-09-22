"""

Given an array remove the nth element from it.

For example: given [1, 5, 6, 7, 9,3, 5, 9].

So, removing 3 should make the array [1, 5, 7, 9, 3, 5, 9].

//arr array from which to remove

//len length of the array

//n nth element to remove

//returns the new length of the array

//Example code

int remove(int arr[], int& len, int n)

{

//Your code
"""


# op: So, removing 3 should make the array [1, 5, 7, 9, 3, 5, 9].

# Example usage
arr = [1, 5, 6, 7, 9, 3, 5, 9]
n = 3


def RemoveNthElem(arr,n):
    if n not in arr:
        return -1
    
    if n in arr:
        arr.remove(n)
    

    print(arr)
    return len(arr)


print(RemoveNthElem(arr,n)) 