# TODO: Add back solution for part 1

# val is beaten by key
beatenBy = {
    "A": "C",
    "B": "A",
    "C": "B"
}

loses = {
    "C": "A",
    "A": "B",
    "B": "C"
}

shapeScores = {
    "A": 1,
    "B": 2,
    "C": 3
}

outcomeScores = {
    "win": 6,
    "loss": 0,
    "draw": 3
}

needsToEndWith = {
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}


def determineShape(opp, outcome):
  if outcome == "win":
    return loses[opp]
  elif outcome == "loss":
    return beatenBy[opp]
  else:
    return opp


def decode(scoreSheet):
  file = open(scoreSheet, 'r')
  lines = file.readlines()

  totalScore = 0

  for line in lines:
    opp, outcome = line.strip().split(' ')
    totalScore += outcomeScores[needsToEndWith[outcome]]
    totalScore += shapeScores[determineShape(opp, needsToEndWith[outcome])]

  return totalScore


if __name__ == "__main__":
  print(decode('testCase.txt'))
