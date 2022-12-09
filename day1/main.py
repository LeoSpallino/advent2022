# TODO: Add back solution for part 1

import heapq


def mostTotalCalories(calorieFile):
  file = open(calorieFile, 'r')
  lines = file.readlines()

  highestTotal = 0
  runningTotal = 0

  for line in lines:
    current = line.strip()
    if current == '':
      if runningTotal > highestTotal:
        highestTotal = runningTotal
      runningTotal = 0
    else:
      runningTotal += int(current)

  if runningTotal > highestTotal:
    highestTotal = runningTotal

  return highestTotal


def topNTotalCalories(calorieFile, N):
  file = open(calorieFile, 'r')
  lines = file.readlines()

  heapOfTotals = []
  runningTotal = 0

  for line in lines:
    current = line.strip()
    if current == '':
      heapq.heappush(heapOfTotals, runningTotal * -1)
      runningTotal = 0
    else:
      runningTotal += int(current)

  if runningTotal > 0:
    heapq.heappush(heapOfTotals, runningTotal * -1)

  topN = 0
  for i in range(N):
    topN += (heapq.heappop(heapOfTotals) * -1)
  return topN


if __name__ == "__main__":
  print(topNTotalCalories('testCase.txt', 3))
