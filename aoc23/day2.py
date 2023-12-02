from utils import read_file
import re


file_path = "day2.txt"
result = read_file(file_path)

cube_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
final_score = 0
finsl_score_power_set = 0
for line in result:
    game_id, outcomes = line.split(":")
    rounds = outcomes.split(";")

    valid_game = True
    color_set = {"red": 0, "green": 0, "blue": 0}
    for each_raound in rounds:
        cubes = each_raound.split(",")
        for cube in cubes:
            color = re.findall(f"(blue|green|red)", cube)[0]
            number_of_cubes = int(re.findall(f"\d+", cube)[0])
            if cube_max[color] < number_of_cubes:
                valid_game = False
            if color_set[color] < number_of_cubes:
                color_set[color] = number_of_cubes

    powe_set = 1
    for val in color_set.values():
        powe_set *= val

    finsl_score_power_set += powe_set

    if valid_game:
        final_score += int(game_id)

print(final_score)
print(finsl_score_power_set)
