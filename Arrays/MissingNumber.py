
def missingNumber(a, N):
    # Summation of first N numbers:
    # N is the No.of Size...
    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(a)

    missingNum = summation - s2
    return missingNum

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


