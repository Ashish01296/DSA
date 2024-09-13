def ReverseString(s1):
    return s1[::-1]



print(ReverseString("Ashish"))




def RevString(s2):
    reverse_str = ""
    for i in range(len(s2),0,-1):
        reverse_str += s2[i-1]
    return reverse_str 




print(RevString("Ashish"))
