def longestCommonPrefix(s):
    if not s:  # Edge case: if the list is empty
        return ""

    # Find the shortest string in the list
    prefix = min(s, key=len)  # min function with key finds the shortest string

    # Initialize result
    result = prefix

    while prefix is not None:
        count = sum(1 for i in s if i.startswith(prefix))  # Count how many strings match the current prefix
        if count == len(s):  # If all strings match
            return prefix
        prefix = prefix[:-1]  # Shorten the prefix one character at a time

    return ""  # Return empty string if no common prefix found


s = ["geeksforgeeks", 'geeks', 'geek', 'geezer']

print(longestCommonPrefix(s))




