def parseInput(puzzleInput):
  formatted = []

  for line in puzzleInput:
    formatted.append([int(height) for height in line])

  return formatted


def part1(forest):
  visibleCount = 0

  for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[i]) - 1):
      up = [x[j] for x in forest[:i]]
      down = [x[j] for x in forest[i+1:]]
      left = forest[i][:j]
      right = forest[i][j+1:]

      if forest[i][j] > max(up):
        visibleCount += 1
        continue
      elif forest[i][j] > max(down):
        visibleCount += 1
        continue
      elif forest[i][j] > max(left):
        visibleCount += 1
        continue
      elif forest[i][j] > max(right):
        visibleCount += 1
        continue

  visibleCount += len(forest) * 2 + (len(forest[0]) - 2) * 2
  return visibleCount


def getScenicScore(height, section):
  currentIndex = 0
  score = 0

  while currentIndex < len(section):
    score += 1
    if height <= section[currentIndex]:
      break
    currentIndex += 1

  return score


def part2(forest):
  highestScenicScore = 0

  for i in range(1, len(forest) - 1):
    for j in range(1, len(forest[i]) - 1):
      up = [x[j] for x in forest[:i]][::-1]
      down = [x[j] for x in forest[i+1:]]
      left = forest[i][:j][::-1]
      right = forest[i][j+1:]

      scenicUp = getScenicScore(forest[i][j], up)
      scenicDown = getScenicScore(forest[i][j], down)
      scenicLeft = getScenicScore(forest[i][j], left)
      scenicRight = getScenicScore(forest[i][j], right)

      scenicScore = scenicUp * scenicDown * scenicLeft * scenicRight

      if scenicScore > highestScenicScore:
        highestScenicScore = scenicScore

  return highestScenicScore


def solve(puzzleInput):
  data = parseInput(puzzleInput)
  solution1 = part1(data)
  solution2 = part2(data)

  return solution1, solution2


if __name__ == '__main__':
  file = open('testCase.txt', 'r')
  puzzleInput = [line.strip() for line in file.readlines()]
  solutions = solve(puzzleInput)
  print("\n".join(str(solution) for solution in solutions))
