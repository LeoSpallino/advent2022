# TODO: Add solutions for part 1 (overwritten)

def checkTotalOverlap(first, sec):
  firstSet = set(range(int(first[0]), int(first[1]) + 1))
  secSet = set(range(int(sec[0]), int(sec[1]) + 1))
  return len(firstSet.intersection(secSet)) > 0


if __name__ == "__main__":
  file = open('testCase.txt', 'r')
  lines = [line.strip() for line in file.readlines()]

  totalOverlaps = 0

  for line in lines:
    first, sec = line.split(',')
    if checkTotalOverlap(first.split('-'), sec.split('-')):
      totalOverlaps += 1

  print(totalOverlaps)
