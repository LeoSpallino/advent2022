from collections import deque


def parseInput(puzzleInput):
  formatted = []

  for line in puzzleInput:
    formatted.append(line)

  return formatted


def part1(data):
  queue = deque([])
  X = 1
  XVals = []

  cycleChecks = [19, 59, 99, 139, 179, 219]
  for i, line in enumerate(data):
    if line == 'noop':
      queue.append(None)
    else:
      add = line.split(' ')[1]
      queue.append(None)
      queue.append(int(add))

  for i in range(len(queue)):
    if i in cycleChecks:
      XVals.append((i+1) * X)
    curr = queue.popleft()
    if curr is not None:
      X += curr

  return sum(XVals)


def part2(data):
  pass


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
