from utils import read_file
import re


file_path = "day1.txt"
result = read_file(file_path)
p1 = 0
p2 = 0

r1 = r"\d"
r2 = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"

decode = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
np1 = 0
np2 = 0
for line in result:
    nums = re.findall(r1, line)
    both = re.findall(r2, line)
    if len(nums) >= 1:
        number = int(nums[0] + nums[-1])
        p1 += number
    if len(both) >= 1:
        first = decode[both[0]] if both[0] in decode else both[0]
        second = decode[both[-1]] if both[-1] in decode else both[-1]
        p2 += int(first + second)

print(p1)
print(p2)
