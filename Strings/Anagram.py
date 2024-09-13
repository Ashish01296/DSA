def Anagram(s1,s2):
    from collections import Counter
    if len(s1)!=len(s2):
        return False
    else:
        s_Counter = Counter(s1)
        t_Counter = Counter(s2)
    return s_Counter==t_Counter




print(Anagram("car","arc"))    # T.C : 0(n)   #S.C: 0(1)



