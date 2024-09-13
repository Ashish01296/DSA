# Check if a number is Palindrome or Not


def NumberPalindrome(n):
        """
        :type x: int
        :rtype: bool
        """

        if n<0:
            return False
        else:
            d = list(str(n))

            d = d[::-1]

            d = int(''.join(d))

            if n==d:
                return True
            else:
                return False
            


print(NumberPalindrome(-121))

