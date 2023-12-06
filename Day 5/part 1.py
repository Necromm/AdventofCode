import math
file = open('Input', 'r')

lines = file.readlines()

codeNumDict = {
    'seed': [int(x) for x in lines.pop(0).split(':')[1].strip().split(' ')],
    'soil': [],
    'fertilizer': [],
    'water': [],
    'light': [],
    'temperature': [],
    'humidity': [],
    'location': []
}

lines.pop(0)

for key in codeNumDict:
    if not codeNumDict[key]:
        codeNumDict[key] = [-math.inf for x in codeNumDict['seed']]

processingFrom = ''
processingTo = ''


def convert_code(source, code_map):
    destination_range_start = code_map[0]
    source_range_start = code_map[1]
    range_length = code_map[2]
    for codeIndex in range(len(source)):
        if source_range_start <= source[codeIndex] < source_range_start + range_length:
            codeNumDict[processingTo][codeIndex] = destination_range_start + source[codeIndex] - source_range_start


def fill_gaps():
    for item in range(len(codeNumDict[processingTo])):
        if codeNumDict[processingTo][item] == -math.inf:
            codeNumDict[processingTo][item] = codeNumDict[processingFrom][item]


for line in lines:
    line = line.strip()
    if len(line) > 1 and not line[0].isnumeric():
        processingFrom = line.split('-')[0]
        processingTo = line.split('-')[2].split(' ')[0]
    elif len(line) > 1 and line[0].isnumeric():
        convert_code(codeNumDict[processingFrom], [int(x) for x in line.split(' ')])
    else:
        fill_gaps()

fill_gaps()

closestLocation = math.inf
for location in codeNumDict['location']:
    if location < closestLocation:
        closestLocation = location
print(codeNumDict['location'])
print(closestLocation)
