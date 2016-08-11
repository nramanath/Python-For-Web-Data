import re

file = open("C:/Users/rnachia/Documents/file_upload.txt")
sum = 0

for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if (len(numbers) > 0):
        print numbers
        for number in numbers:
            sum += int(number)

print sum