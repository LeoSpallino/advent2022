# TODO: Add back solution for part 1

def findCommonTypes(rucksacks):
  common = set(rucksacks[0])
  for rucksack in range(1, len(rucksacks)):
    common = common & set(rucksacks[rucksack])
  return [commonType for commonType in common][0]


def getPriority(letter):
  ascii_val = ord(letter)

  if ascii_val < 91:
    return ascii_val - 65 + 27
  else:
    return ascii_val - 97 + 1


if __name__ == "__main__":
  file = open('testCase.txt', 'r')
  lines = [line.strip() for line in file.readlines()]
  teamSize = 3

  totalPriority = 0

  for i in range(0, len(lines), teamSize):
    totalPriority += getPriority(findCommonTypes(lines[i:i+3]))

  print(totalPriority)
