import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

elf = {}
i = 1
calories = 0

with open('calories.txt') as f:
    for line in f:
        logging.info(f'processing line {i}')
        if line.strip() == "":
            logging.info(f'blank line: assigning {calories} calories to elf {i}')
            elf[i] = calories
            calories = 0
            i += 1
        else:
            logging.info(f'calorie count for elf {i} is {calories}, adding {line}')
            calories += int(line)

logging.info(f'elves: {elf}')

top_three = sorted(elf.items(), key=lambda x:x[1])[-3:]
their_calories = 0
for elf in top_three:
    their_calories += elf[1]

print(f'Top three elves are carrying {top_three}: sum is {their_calories}')