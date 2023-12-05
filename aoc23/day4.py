#!/usr/bin/env python3
from utils import read_file
import re


file_path = "day4.txt"
result = read_file(file_path)

p1 = 0
p2 = 0
copies = {i: 1 for i in range(len(result))}
for i, line in enumerate(result):
    winning, yours = line.split("|")
    winning = set(map(int, re.findall(r"\d{1,2}", winning)))
    yours = list(map(int, re.findall(r"\d{1,2}", yours)))
    winners = 0
    for number in yours:
        if number in winning:
            winners += 1

    for _ in range(copies[i]):
        if winners:
            for j in range(1, winners + 1):
                copies[i + j] += 1

    score = 2 ** (winners - 1) if winners else 0

    p1 += score
    p2 += copies[i]

print(p1)
print(p2)
