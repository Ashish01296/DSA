class Solution(object):
    def nextGreaterElements(self, nums):
            n = len(nums)
            nge = [-1] * n
            st = []


            for i in range((2 * n - 1) , -1, -1):
                while st  and st[-1] <= nums[i % n]:
                    st.pop()


                if i < n:
                    if st:
                        nge[i] = st[-1]
                st.append(nums[i % n])
            return nge
