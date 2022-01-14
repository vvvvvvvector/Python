pairs = ('AT', 'TA', 'CG', 'GC')


def reverse(str):
    return str[::-1]


def compare(first_str, second_str):
    pairsAmount = 0
    i = 0
    while first_str[i] != '-':
        if first_str[i] != '*' and second_str[i] != '*':
            pair = (first_str[i] + second_str[i])
            if pair in pairs:
                pairsAmount += 1
        i += 1
    return pairsAmount


def hairpin(primer, head):
    nMaxPairs = 0
    for i in range(1, len(primer[head * 2:])):
        firstStr = primer[:i]
        secondStr = primer[i:]
        slicedSecondStr = reverse(secondStr[head * 2:])
        secondStrEnd = secondStr[:head * 2]
        firstStrEnd = secondStrEnd[:head]
        slicedSecondStrEnd = reverse(secondStrEnd[-head:])
        if(len(slicedSecondStr) - len(firstStr) >= 0):
            first_str = '*' * (len(slicedSecondStr) -
                               len(firstStr)) + firstStr + '-' + firstStrEnd
            second_str = slicedSecondStr + '-' + slicedSecondStrEnd + '\n'

            pairsAmount = compare(first_str, second_str)

            if(nMaxPairs < pairsAmount):
                nMaxPairs = pairsAmount
        else:
            first_str = firstStr + '-' + firstStrEnd
            second_str = '*' * (len(firstStr) - len(slicedSecondStr)) + \
                slicedSecondStr + '-' + slicedSecondStrEnd + '\n'

            pairsAmount = compare(first_str, second_str)

            if(nMaxPairs < pairsAmount):
                nMaxPairs = pairsAmount

    return nMaxPairs


def main():
    file_primers = open('Files/primers.txt', 'r')
    file_result = open('Files/result.txt', 'w')

    for line in file_primers:
        hairpinResult = hairpin(line.strip(), 2)
        file_result.write('{} {}\n'.format(line.strip(), hairpinResult))
    print('Writing to the file was successful!')

    file_primers.close()
    file_result.close()


if __name__ == "__main__":
    main()
