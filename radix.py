from typing import Counter
import time

def max_char(input):
    max_char = max(map(len, input))
    return max_char

def count_radix_sort(input, n, pos, base):
    ordered_input = [0]*n 
    count_vector = [0]*(base+1)
    conv_base = ord("A")-1

    for word in input:
        if pos < len(word):
            pos_letter = ord(word[pos]) - conv_base
            count_vector[pos_letter] += 1
        else:
            pos_letter = 0
    
    for i in range(base):
        count_vector[i+1] += count_vector[i]

    for word in reversed(input):
        if pos < len(word):
            pos_letter = ord(word[pos]) - conv_base
        else:
            pos_letter = 0
        ordered_input[count_vector[pos_letter]-1] = word
        count_vector[pos_letter] -= 1
    
    return ordered_input

def radix_sort(input):
    max_digit = max_char(input)
    for i in range(max_digit-1, -1, -1):
        input = count_radix_sort(input, len(input), i, 26)

    return input

def is_valid(word):
    if len(word) < 4:
        return False
    else:
        for char in word:
            if not "A" <= char <= "Z":
                return False
        return True

start = time.time()
print("ordenando frankenstein...")
with open("frankestein_clean.txt", "r") as file:
    list_words = []
    for line in file:
        for word in line.split():
            if is_valid(word):
                list_words.append(word)

word_sorted = radix_sort(list_words)
word_frequency = dict(Counter(word for word in word_sorted))

with open("frankenstein_ordenado.txt", "w") as out:
    for key in word_frequency:
        out.write(f"{key} {word_frequency[key]}\n")
print(f"frankenstein lido e ordenado em {time.time()-start} segundos")

start = time.time()
print("ordenando war and peace...")
with open("war_and_peace_clean.txt", "r") as file:
    list_words = []
    for line in file:
        for word in line.split():
            if is_valid(word):
                list_words.append(word)

word_sorted = radix_sort(list_words)
word_frequency = dict(Counter(word for word in word_sorted))

with open("war_and_peace_ordenado.txt", "w") as out:
    for key in word_frequency:
        out.write(f"{key} {word_frequency[key]}\n")
print(f"war and peace lido e ordenado em {time.time()-start} segundos")

