pairs = ('AT', 'TA', 'CG', 'GC')


def reverse(str):
    return str[::-1]


def compare(first_str, second_str):
    pairsAmount = 0
    for i in range(len(first_str)):
        if first_str[i] != '*' and second_str[i] != '*':
            pair = (first_str[i] + second_str[i])
            if pair in pairs:
                pairsAmount += 1
    return pairsAmount


def hairpin(primer):
    nMaxPairs = 0
    for i in range(1, len(primer)):
        if(len(reverse(primer[i:])) - len(primer[:i]) >= 0):
            first_str = '*' * \
                (len(reverse(primer[i:])) - len(primer[:i])) + primer[:i]
            second_str = reverse(primer[i:])

            pairsAmount = compare(first_str, second_str)

            if(nMaxPairs < pairsAmount):
                nMaxPairs = pairsAmount

            print(pairsAmount)
            print(first_str)
            print(second_str + '\n')
        else:
            first_str = primer[:i]
            second_str = '*' * \
                (len(primer[:i]) - len(primer[i:])) + reverse(primer[i:])

            pairsAmount = compare(first_str, second_str)

            if(nMaxPairs < pairsAmount):
                nMaxPairs = pairsAmount

            print(pairsAmount)
            print(first_str)
            print(second_str + '\n')

    return nMaxPairs


def main():
    str = 'TACCGGTAGGACTACTGGTA'

    print(hairpin(str))


if __name__ == "__main__":
    main()
