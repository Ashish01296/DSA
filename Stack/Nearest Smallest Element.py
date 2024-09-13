class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        smallestele = [-1] * n
        st = []
        
        for i in range(n):
            while st and st[-1] >= A[i]:
                st.pop()
            
            if st:
                smallestele[i] = st[-1]
            st.append(A[i])
        
        return smallestele


