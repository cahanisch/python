import re

def matchRegex(regex, numSet):
    for z in numSet:
        if re.match(regex, z) is not None:
            print(z, "is a match!")
        else:
            print(z, "is not a match")


def main():
    prob1set1 = ['11011', '1010101', '1', '111111111']
    prob1set2 = ['101010', '1111', '00']

    prob1regex = '^((0|1)((0|1)(0|1))*)$'

    print("-------- Problem 1 Set 1 ---------")
    matchRegex(prob1regex, prob1set1)
    print("\n-------- Problem 1 Set 2 ---------")
    matchRegex(prob1regex, prob1set2)

    prob2set1 = ['10010','10101110','1001','011']
    prob2set2 = ['100010','000','1111','1000']

    prob2regex = '^((1?(01)*00(10)*1?)|(0?(10)*11(01)*0?))$'

    print("\n-------- Problem 2 Set 1 ---------")    
    matchRegex(prob2regex, prob2set1)
    print("\n-------- Problem 2 Set 2 ---------")
    matchRegex(prob2regex, prob2set2)

    prob3set1 = ['42', '307', '1337', '8675309']
    prob3set2 = ['111', '313', '12345', '678910']

    prob3regex = '^(([02468]*[13579][02468]*[13579][02468]*)+|[02468]+)$'

    print("\n-------- Problem 3 Set 1 ---------")
    matchRegex(prob3regex, prob3set1)
    print("\n-------- Problem 3 Set 2 ---------")
    matchRegex(prob3regex, prob3set2)

    prob4set1 = ['010', '1000', '000', '0001000']
    prob4set2 = ['0011', '1100', '101010', '0']

    prob4regex = '^((1?00+)|(0+1?0+)|(00+1?))$'

    print("\n-------- Problem 4 Set 1 ---------")
    matchRegex(prob4regex, prob4set1)
    print("\n-------- Problem 4 Set 2 ---------")
    matchRegex(prob4regex, prob4set2)

    prob5set1 = ['Super1337h@xor!', 'Elitehacker1234%', 'Ihaveh@x','Enoughh@xjokes4242!']

    #added in h@x as a nessecary part of the passphrase
    prob5regex = '^((?=.*[A-Z][a-z]*)(?=.*[0-9]{4})(?=.*[!@#%&])?(?=.*[h][@][x])).{10,20}$'

    print("\n-------- Problem 4 Set 1 ---------")
    matchRegex(prob5regex, prob5set1)

if __name__ == "__main__":
    main()