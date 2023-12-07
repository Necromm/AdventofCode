'''
--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
'''

import math
file = open('Input', 'r')

lines = file.readlines()

seedNums = [int(x) for x in lines.pop(0).split(':')[1].strip().split(' ')]

codeNumDict = {
    'seed': [],
    'soil': [],
    'fertilizer': [],
    'water': [],
    'light': [],
    'temperature': [],
    'humidity': [],
    'location': []
}

processingFrom = ''
processingTo = ''


def init_seed():
    seed_ranges = []
    for x in range(len(seedNums[::2])):
        seed_ranges.append((seedNums[2*x], seedNums[2*x]+seedNums[2*x+1]-1))
    codeNumDict['seed'] = seed_ranges


def update_dict(key, item):
    codeNumDict[key].append(item)


def convert_code(source, code_map):
    source_min = source[0]
    source_max = source[1]

    destination_range_min = code_map[0]
    source_range_min = code_map[1]
    range_length = code_map[2]
    destination_range_max = destination_range_min + range_length - 1
    source_range_max = source_range_min + range_length - 1

    if source_min > source_range_max or source_max < source_range_min:
        return [source]
    elif source_min < source_range_min:
        if source_max > source_range_max:
            update_dict(processingTo, (destination_range_min,
                                       destination_range_max))

            return [(source_min, source_range_min-1),(source_range_max+1, source_max)]
        else:
            update_dict(processingTo, (destination_range_min,
                                       source_max-source_range_min+destination_range_min))

            return [(source_min, source_range_min-1)]
    else:
        if source_max > source_range_max:
            update_dict(processingTo, (source_min-source_range_min+destination_range_min,
                                       destination_range_max))

            return [(source_range_max+1,source_max)]
        else:
            update_dict(processingTo, (source_min-source_range_min+destination_range_min,
                                       source_max-source_range_min+destination_range_min))

            return []


init_seed()
lines.pop(0)


def convert_leftovers():
    codeNumDict[processingTo] += codeNumDict[processingFrom]


unprocessedRanges = []

for line in lines:
    line = line.strip()
    if len(line) > 1 and not line[0].isnumeric():
        processingFrom = line.split('-')[0]
        processingTo = line.split('-')[2].split(' ')[0]
    elif len(line) > 1 and line[0].isnumeric():
        for numRange in range(len(codeNumDict[processingFrom])):
            unprocessedRanges += convert_code(codeNumDict[processingFrom].pop(0), [int(x) for x in line.split(' ')])
    else:
        convert_leftovers()
    codeNumDict[processingFrom] += unprocessedRanges
    unprocessedRanges = []

convert_leftovers()

closestLocation = math.inf
for location in codeNumDict['location']:
    if location[0] < closestLocation:
        closestLocation = location[0]
print(codeNumDict['location'])
print(closestLocation)




