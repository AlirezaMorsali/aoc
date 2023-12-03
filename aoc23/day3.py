#!/usr/bin/env python3
from utils import read_file
import string
import re

symbols = set(string.punctuation)
symbols.remove(".")

print("Manually added empty lines with . as the first and last line")

max_len = 140
file_path = "day3.txt"

result = read_file(file_path)


def find_gear(current, prev_line, next_line, gear_dict, current_index):
    numbers = re.findall(r"\d+", current)
    start = 0
    for number in numbers:
        start = start + current[start:].find(number)
        end = start + len(number)
        new_start = start - 1 if start > 0 else 0
        new_end = end + 1 if end < max_len else max_len
        start = end

        for index in range(new_start, new_end):
            if prev_line[index] == "*":
                if (current_index - 1, index) in gear_dict:
                    gear_dict[(current_index - 1, index)].append(number)
                else:
                    gear_dict[(current_index - 1, index)] = [number]
            if next_line[index] == "*":
                if (current_index + 1, index) in gear_dict:
                    gear_dict[(current_index + 1, index)].append(number)
                else:
                    gear_dict[(current_index + 1, index)] = [number]
            if current[index] == "*":
                if (current_index, index) in gear_dict:
                    gear_dict[(current_index, index)].append(number)
                else:
                    gear_dict[(current_index, index)] = [number]


def sum_current_line(current, prev_line, next_line):
    numbers = re.findall(r"\d+", current)
    start = 0
    summation = 0
    for number in numbers:
        start = start + current[start:].find(number)
        end = start + len(number)
        new_start = start - 1 if start > 0 else 0
        new_end = end + 1 if end < max_len else max_len
        start = end
        if (
            any([char in symbols for char in prev_line[new_start:new_end]])
            or any([char in symbols for char in next_line[new_start:new_end]])
            or any([char in symbols for char in current[new_start:new_end]])
        ):
            summation += int(number)
    return summation


final_score = 0
gear_dict = {}
for i in range(1, len(result) - 1):
    prev_line = result[i - 1]
    current = result[i]
    next_line = result[i + 1]

    final_score += sum_current_line(current, prev_line, next_line)
    find_gear(current, prev_line, next_line, gear_dict, i)

p2_score = 0
for gear, vals in gear_dict.items():
    if len(vals) == 2:
        p2_score += int(vals[0]) * int(vals[1])

print(final_score)
print(p2_score)
