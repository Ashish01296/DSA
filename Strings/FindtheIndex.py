haystack = "sadbutsad"
needle = "sad"

c = []
for i in range(len(haystack)):
            for j in range(len(needle)):
                if haystack[i]==needle[j]:
                       c.append(i)


print(c[0])
                    