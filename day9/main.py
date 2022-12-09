class Point:
  def __init__(self, nextKnot=None):
    self.X = 0
    self.Y = 0
    self.nextKnot = nextKnot

  def getCoord(self):
    return (self.X, self.Y)

  def getNextKnot(self):
    return self.nextKnot


class Rope:
  def __init__(self):
    self.head = Point()
    self.tail = Point()
    self.visited = {self.tail.getCoord()}

  def _shouldTailMove(self):
    headX, headY = self.head.getCoord()
    tailX, tailY = self.tail.getCoord()

    if abs(headX - tailX) > 1 or abs(headY - tailY) > 1:
      return True
    return False

  def _moveTail(self, direction):
    match direction:
      case 'U':
        self.tail.X = self.head.X
        self.tail.Y += 1
      case 'D':
        self.tail.X = self.head.X
        self.tail.Y -= 1
      case 'L':
        self.tail.Y = self.head.Y
        self.tail.X -= 1
      case 'R':
        self.tail.Y = self.head.Y
        self.tail.X += 1

    self.visited.add(self.tail.getCoord())

  def moveHead(self, direction, amount):
    for _ in range(amount):
      match direction:
        case 'U':
          self.head.Y += 1
        case 'D':
          self.head.Y -= 1
        case 'L':
          self.head.X -= 1
        case 'R':
          self.head.X += 1
      if self._shouldTailMove():
        self._moveTail(direction)


def part1(data):
  rope = Rope()

  for direction, amount in data:
    rope.moveHead(direction, amount)

  return len(rope.visited)


def part2(data):
  pass


def parseInput(puzzleInput):
  formatted = []

  for line in puzzleInput:
    direction, amount = line.split(' ')
    formatted.append((direction, int(amount)))

  return formatted


def solve(puzzleInput):
  data = parseInput(puzzleInput)
  solution1 = part1(data)
  solution2 = part2(data)

  return solution1, solution2


if __name__ == '__main__':
  file = open('testCase1.txt', 'r')
  puzzleInput = [line.strip() for line in file.readlines()]
  solutions = solve(puzzleInput)
  print("\n".join(str(solution) for solution in solutions))
