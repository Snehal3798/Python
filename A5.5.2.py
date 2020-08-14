def ChkPrime(lst):
    arr = []
    for i in lst:
        isPrime = True
        for no in range(2,i):
            if i%2==0:
                isPrime = False
                break

            if isPrime:
                arr.append(i)
        print("Prime no are",arr)
        print("Sum is",sum(arr))
