pairs = ('AT', 'TA', 'CG', 'GC')


def reverse(str):
    return str[::-1]


def compare(first_str, second_str):
    max = 0
    for i in range(len(first_str)):
        if first_str[i] != '*' and second_str[i] != '*':
            pair = (first_str[i] + second_str[i])
            if pair in pairs:
                max += 1
    return max


def hairpin(primer):
    nMaxPairs = 0
    for i in range(1, len(primer)):
        if(len(reverse(primer[i:])) - len(primer[:i]) >= 0):
            first_str = '*' * \
                (len(reverse(primer[i:])) - len(primer[:i])) + primer[:i]
            second_str = reverse(primer[i:])

            currentMAX = compare(first_str, second_str)

            if(nMaxPairs < currentMAX):
                nMaxPairs = currentMAX

            print(currentMAX)
            print(first_str)
            print(second_str + '\n')
        else:
            first_str = primer[:i]
            second_str = '*' * \
                (len(primer[:i]) - len(primer[i:])) + reverse(primer[i:])

            currentMAX = compare(first_str, second_str)

            if(nMaxPairs < currentMAX):
                nMaxPairs = currentMAX

            print(currentMAX)
            print(first_str)
            print(second_str + '\n')

    return nMaxPairs


def main():
    str = 'TACCGGTAGGACTACTGGTA'

    print(hairpin(str))


if __name__ == "__main__":
    main()
