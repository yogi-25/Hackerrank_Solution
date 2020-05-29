
def check(string):
    # set function convert string
    # into set of characters .
    p = set(string)
    print(p)
    # declare set of '0', '1' .
    s = {'0', '1'}

    # check set p is same as set s
    # or set p contains only '0'
    # or set p contains only '1'
    # or not, if any one condition
    # is true then string is accepted
    # otherwise not .
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")

    # driver code


from itertools import permutations

# Initialising string
ini_str = "abc"

# Printing initial string
print("Initial string", ini_str)

# Finding all permuatation
permutation = [''.join(p) for p in permutations(ini_str)]
# Printing result
print("Resultant List", str(permutation))
d=2
ini_str = "abc"
print(ini_str.split(ini_str,d))
# Printing initial string
print("Initial string", ini_str)

# Finding all permuatation
result = []

def permute(data, i, d):
    if i == d:
        result.append(''.join(data))
    else:
        for j in range(i, d):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, d)
            data[i], data[j] = data[j], data[i]


permute(list(ini_str), 0, len(ini_str))
import re
print("Resultant permutations", str(result))
#substring(ini_str, seq(1, 9, 2), seq(2, 1


if __name__ == "__main__":
    string = input()

    # function calling
    check(string)
