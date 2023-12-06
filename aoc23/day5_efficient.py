#!/usr/bin/env python3
#!/usr/bin/env python3
from utils import read_file
from tqdm import tqdm
import re
import numpy as np


class Mapping:
    def __init__(self, source_to_dest: str) -> None:
        self.s2d = source_to_dest
        self.dest2source = {}
        self.source2dest = {}
        self.ranges = []
        self.starts = []
        self.ends = []

    def add_range(self, this_range: str):
        dest, source, length = list(map(int, this_range.split(" ")))

        self.ranges.append(
            (range(dest, dest + length + 1), range(source, source + length + 1))
        )
        self.starts.append(source)
        self.ends.append(source + length + 1)

    def get_range(self, source_start, source_end):
        dest_ranges = []
        starts = self.starts
        indices = sorted(range(len(starts)), key=lambda i: starts[i])
        while source_start <= source_end:
            for index in indices:
                this_range = self.ranges[index]
                s_end = None
                if source_start < this_range[1][0]:
                    s_end = this_range[1][0]
                elif source_start in this_range:
                    if source_end in this_range:
                        s_end = source_end
                    else:
                        s_end = self.get_dest(this_range[1][-1])
                if s_end:
                    dest_ranges.append(
                        (self.get_dest(source_start), self.get_dest(s_end))
                    )
                    source_start = s_end + 1

            if all(map(lambda x: x > source_start, self.ends)):
                dest_ranges.append(
                    (self.get_dest(source_start), self.get_dest(source_end))
                )
                source_start = source_end + 1
        return dest_ranges

    def get_dest(self, source):
        for this_range in self.ranges:
            if source in this_range[1]:
                index = this_range[1].index(source)
                return this_range[0][index]
        return source

    def get_source(self, dest):
        for this_range in self.ranges:
            if dest in this_range[0]:
                index = this_range[0].index(dest)
                return this_range[1][index]
        return dest

    def slow_add_range(self, this_range: str):
        dest, source, length = list(map(int, this_range.split(" ")))
        for d, s in zip(
            range(dest, dest + length + 1), range(source, source + length + 1)
        ):
            self.dest2source[d] = s
            self.source2dest[s] = d

    def slow_get_dest(self, source):
        if source in self.source2dest:
            return self.source2dest[source]
        else:
            return source

    def slow_get_source(self, dest):
        if dest in self.dest2source:
            return self.dest2source[dest]
        else:
            return dest


m = Mapping("1")
m.add_range("50 98 2")
m.add_range("52 50 48")
m.get_range(0, 10)

# # file_path = "5day5.txt"
# # file_path = "day5.txt"

# result = read_file(file_path)
# mapping = {}
# for line in tqdm(result, desc="Building mappings"):
#     if line.startswith("seeds:"):
#         place = "1"
#     elif line.startswith("seed-to-soil"):
#         place = "1:2"
#         mapping[place] = Mapping(place)
#     elif line.startswith("soil-to-fertilizer"):
#         place = "2:3"
#         mapping[place] = Mapping(place)
#     elif line.startswith("fertilizer-to-water"):
#         place = "3:4"
#         mapping[place] = Mapping(place)
#     elif line.startswith("water-to-light"):
#         place = "4:5"
#         mapping[place] = Mapping(place)
#     elif line.startswith("light-to-temperature"):
#         place = "5:6"
#         mapping[place] = Mapping(place)
#     elif line.startswith("temperature-to-humidity"):
#         place = "6:7"
#         mapping[place] = Mapping(place)
#     elif line.startswith("humidity-to-location"):
#         place = "7:8"
#         mapping[place] = Mapping(place)
#     else:
#         if place == "1":
#             if line:
#                 seeds = list(map(int, line.split(" ")))
#         else:
#             if line:
#                 mapping[place].add_range(line)

# loc_to_seed = {}
# for seed in tqdm(seeds, desc="Tracking seeds"):
#     source = seed
#     for i in range(1, 8):
#         dest = mapping[f"{i}:{i+1}"].get_dest(source)
#         source = dest
#     loc_to_seed[source] = seed

# print(f"P1: {min(loc_to_seed.keys())}")

# allseeds = []
# for i in tqdm(range(0, len(seeds), 2), desc="All seeds"):
#     new_seeds = list(range(seeds[i], seeds[i] + seeds[i + 1] + 1))
#     allseeds.extend(new_seeds)

# print(f"Len all seeds: {len(allseeds)}")
# loc_to_seed = {}
# for seed in tqdm(allseeds, desc="Tracking all seeds"):
#     source = seed
#     for i in range(1, 8):
#         dest = mapping[f"{i}:{i+1}"].get_dest(source)
#         source = dest
#     loc_to_seed[source] = seed

# print(f"P2: {min(loc_to_seed.keys())}")
