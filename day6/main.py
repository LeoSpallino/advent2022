def part1(data):
  for i in range(len(data)):
    unique = set(data[i:i+4])
    if len(unique) == 4:
      return i + 4


def part2(data):
  for i in range(len(data)):
    unique = set(data[i:i+14])
    if len(unique) == 14:
      return i + 14


def solve(puzzleInput):
  solution1 = part1(puzzleInput[0])
  solution2 = part2(puzzleInput[0])

  return solution1, solution2


if __name__ == '__main__':
  file = open('testCase.txt', 'r')
  puzzleInput = [line.strip() for line in file.readlines()]
  solutions = solve(puzzleInput)
  print("\n".join(str(solution) for solution in solutions))
