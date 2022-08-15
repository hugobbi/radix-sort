from audioop import reverse
from itertools import count


def max_char(input):
    max_char = max(map(len, input))
    return max_char

def radix_sort(input, base, max_char, pos):
    if pos == max_char:
      return input
    n = len(input)
    ordered_input = [0]*n
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
        ordered_input[count_vector[pos_letter]-1] = word
        count_vector[pos_letter] -= 1

    print(count_vector)
    print(ordered_input)
    pos += 1
    radix_sort(ordered_input, base, max_char, pos)

input = ["OLA", "JORGE", "KA", "ABC"]
base = 26

max_char = max_char(input)
radix_sort(input, base, max_char, 0)
