# def Anagram(s1,s2):
#     from collections import Counter
#     if len(s1)!=len(s2):
#         return False
#     else:
#         s_Counter = Counter(s1)
#         t_Counter = Counter(s2)
#     return s_Counter==t_Counter




# print(Anagram("car","arc"))    # T.C : 0(n)   #S.C: 0(1)


# Brute Force Approache ..........................
def char_frequency_dict(s):
    freq_dict = {}
    #Iterate over each character in the string
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    return freq_dict
# Example strings
s1 = "car"
s2 = "rac"
# Create frequency dictionaries for both strings
freq_s1 = char_frequency_dict(s1)
freq_s2 = char_frequency_dict(s2)
print(freq_s1)  # Output: {'c': 1, 'a': 1, 'r': 1}
print(freq_s2)  # Output: {'r': 1, 'a': 1, 'c': 1}
# Check if the two frequency dictionaries are the same
if freq_s1 == freq_s2:
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")









