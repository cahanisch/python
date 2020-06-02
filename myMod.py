def myMod(num, power, modulo):
    remainder = 1
    while power > 0:
        if power % 2 == 1:
            remainder = remainder * num % modulo
        num = num**2 % modulo
        power = power // 2
    return remainder     

def main():
    #Problem 2
    answer = myMod(11, 143, 25)
    print("11^143 mod 25 = ", answer)
    answer = myMod(42, 143, 313)
    print("42^143 mod 313 = ", answer)
    answer = myMod(1337, 54321, 7331)
    print("1337^54321 mod 7331 = ", answer)
    answer = myMod(1337, 8675309, 10003130001)
    print("1337^8675309 mod 10003130001 = ", answer)
    print("-------------------------------------------")
    #Problem 3    
    answer = myMod(2, 1337, 8675309)
    print("2^1337 mod 8675309 = ", answer)
    answer = myMod(2, 7331, 8675309)
    print("2^7331 mod 8675309 = ", answer)
    answer = myMod(2465938, 1337, 8675309)
    print("2465938^1337 mod 8675309 = ", answer)
    answer = myMod(2610912, 7331, 8675309)
    print("2610912^7331 mod 8675309 = ", answer)

    #Problem 4
    A = 1141
    B = 4294
    a = 2
    p = 7331
    print("-------------------------------------------")
    while (2**a % p) != A: 
        a += 1
    print("Secret Key: ", a)
    answer = myMod(B, a, p)
    print("Shared Secret: ", answer)


main()