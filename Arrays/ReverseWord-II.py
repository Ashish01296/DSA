s =  "Mr Ding"

def reverseWords(self, s):
        def reverse_word(word):
            return word[::-1  ] # "rM gniD"

        eg = s.split()
        reversed_words = [reverse_word(word) for word in eg]
        return " ".join(reversed_words)
       

# "rM gniD"


print(s.split())
