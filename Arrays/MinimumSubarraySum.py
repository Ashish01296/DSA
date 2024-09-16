a = [23, 2, 4, -6, 7]

def MinimumSubarraySum(array):
    current_sum = 0
    min_sum = array[0]  # Initialize to the first element (for edge cases)

    for i in range(0, len(array)):
        current_sum = current_sum + array[i]
        min_sum = min(current_sum, min_sum)

        if current_sum > 0:
            current_sum = 0

    return min_sum

print(MinimumSubarraySum(a))  # Output will be -6, as it is the minimum subarray sum
