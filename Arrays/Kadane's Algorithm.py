#Kadane's Algorithm to FindOut Maximum Sum of Subarray

#0(n) Solution Approach: 

a =[5,4,-1,7,8]


def MaximumSubarraySum(array):
    sum = 0
    max_sum = array[0] # bcz atleast ek number hovo joiye list ma no..

    #for java,c++ you can consider INT_MIN

    for i in range(0,len(array)):
        sum = sum + array[i]
        max_sum = max(sum,max_sum)

        if(sum<0):
            sum = 0
    return max_sum




print(MaximumSubarraySum(a))

