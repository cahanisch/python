def isPrime(y):
    if y == 2:
        return True
    elif y == 1 or y % 2 == 0:
        return False
    for i in range(3, y//2 + 1, 2):
        if y % i == 0:
            return False
    return True

def main():
    x = int(input("Enter a number: "))
    count = 0
    for i in range(1, x+1):
        if isPrime(i) is True:
            if isPrime(i - 2) is True:
                count += 1   
    print("Result: ", count)

if __name__ == "__main__":
    main()