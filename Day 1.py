file = open('Day 1 Input', 'r')

lines = file.readlines()

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
text = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
calVals = []

for line in lines:
    numberFound = False
    firstVal = ''
    lastVal = ''
    firstIndex = 0
    lastIndex = 0
    for n in range(9):
        if number[n] in line:
            if not numberFound:
                numberFound = True
                firstVal = number[n]
                lastVal = number[n]
                firstIndex = line.index(number[n])
                lastIndex = line.rindex(number[n])
            if line.index(number[n]) < firstIndex:
                firstVal = number[n]
                firstIndex = line.index(number[n])
            if line.rindex(number[n]) > lastIndex:
                lastVal = number[n]
                lastIndex = line.rindex(number[n])
        if text[n] in line:
            if not numberFound:
                numberFound = True
                firstVal = number[n]
                lastVal = number[n]
                firstIndex = line.index(text[n])
                lastIndex = line.rindex(text[n])
            if line.index(text[n]) < firstIndex:
                firstVal = number[n]
                firstIndex = line.index(text[n])
            if line.rindex(text[n]) > lastIndex:
                lastVal = number[n]
                lastIndex = line.rindex(text[n])
    calVals.append(firstVal + lastVal)
# print(calVals)
total = 0
for n in calVals:
    total += int(n)

print(total)