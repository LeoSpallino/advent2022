class Point:
  def __init__(self):
    self.X = 0
    self.Y = 0
    self.visited = {(self.X, self.Y)}

  def getCoord(self):
    return (self.X, self.Y)

  def move(self, direction):
    self.X += moves[direction]['X']
    self.Y += moves[direction]['Y']

  def follow(self, point):
    deltaX = point.X - self.X
    deltaY = point.Y - self.Y
    distance = max(abs(deltaX), abs(deltaY))
    if distance > 1:
      if abs(deltaX) == abs(deltaY):
        self.X += deltaX / abs(deltaX)
        self.Y += deltaY / abs(deltaY)
      else:
        if deltaX > 1:
          self.X += 1
          self.Y = point.Y
        if deltaX < -1:
          self.X -= 1
          self.Y = point.Y
        if deltaY > 1:
          self.X = point.X
          self.Y += 1
        if deltaY < -1:
          self.X = point.X
          self.Y -= 1
    self.visited.add((self.X, self.Y))


moves = {
    'U': {
        'X': 0,
        'Y': 1
    },
    'D': {
        'X': 0,
        'Y': -1
    },
    'L': {
        'X': -1,
        'Y': 0,
    },
    'R': {
        'X': 1,
        'Y': 0
    }
}


def part1(data):
  head = Point()
  tail = Point()

  for direction, amount in data:
    for i in range(amount):
      head.move(direction)
      tail.follow(head)

  return len(tail.visited)


def part2(data):
  knots = [Point() for _ in range(10)]
  for direction, amount in data:
    for _ in range(amount):
      knots[0].move(direction)
      for j in range(1, len(knots)):
        knots[j].follow(knots[j-1])

  return len(knots[-1].visited)


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
  file = open('testCase.txt', 'r')
  puzzleInput = [line.strip() for line in file.readlines()]
  solutions = solve(puzzleInput)
  print("\n".join(str(solution) for solution in solutions))
