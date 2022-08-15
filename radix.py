from audioop import reverse
from itertools import count


def max_char(input):
    max_char = max(map(len, input))
    return max_char

def radix_sort(input, base, hi, lo, pos):
    n = len(input)
    ordered_input = []
    count_vector = [0]*base
    conv_base = ord("A")

    for word in input:
        if pos < len(word):
            pos_letter = ord(word[pos]) - conv_base
            count_vector[pos_letter] += 1
    
    print(count_vector)
    for i in range(1, base):
        count_vector[i] += count_vector[i-1]

    print(count_vector)

    for word in reversed(input):
        if pos < len(word):
            pos_letter = ord(word[pos]) - conv_base
        ordered_input[count_vector[pos_letter]] = word
        count_vector[pos_letter] -= 1

    print(count_vector)
    print(ordered_input)
    return ordered_input

input = ["OLA", "JORGE", "KA", "ABC"]
base = 26

radix_sort(input, base, 1, 2, 0)