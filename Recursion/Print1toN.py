def PrintNumber(n):
    if n==0:
        return 0
    else:
        PrintNumber(n-1)
        print(n)


PrintNumber(10)