import pandas as pd
file_contents = []
FILE_NAME = "advent_of_code_1.txt"

df = pd.read_csv(FILE_NAME, header=None, names=['Line'])

file_contents = df['Line'].tolist()

# print(file_contents)
# Part 2
digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def find_first_number(word, is_reverse=False):
    left = 0
    right = 0
    while left < len(word):
        if is_reverse and word[left:right][::-1] in digits:
            return str(digits[word[left:right][::-1]])
        elif not is_reverse and word[left:right] in digits:
            return str(digits[word[left:right]])
        elif word[left].isdigit():
            return word[left]
        else:
            right += 1
            if right - left > 5 or right >= len(word):
                left += 1
                right = left

sum_ = 0
for word in file_contents:
    first_digit = find_first_number(word)
    last_digit = find_first_number(word[::-1], True)
    sum_ += int(first_digit + last_digit)
print(sum_)

"""
# Part 1

sum_ = 0
for word in file_contents:
    for ch in word:
        if ch.isdigit():
            first_digit = ch
            break
    for i in range(len(word) - 1, -1, -1):
        ch = word[i]
        if ch.isdigit():
            last_digit = ch
            break
    sum_ += int(first_digit + last_digit)
print(sum_)
"""
