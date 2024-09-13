# Reverse a Digit

class Solution(object):
    def reverse(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Convert the number to a string and check if it's negative
        if N < 0:
            # Handle the negative number: remove the minus sign, reverse the digits, then add the minus sign back
            N = list(str(N)[1:])  # Skip the minus sign
            N = N[::-1]  # Reverse the digits
            reversed_number = int('-' + ''.join(N))  # Convert back to an integer with the negative sign
        else:
            # For positive numbers, just reverse the digits
            N = list(str(N))
            N = N[::-1]
            reversed_number = int(''.join(N))
        
        # Return the reversed number
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if reversed_number >  INT_MAX or reversed_number <  INT_MIN:
            return 0
        
        return reversed_number


# T.C : O(Logn)

