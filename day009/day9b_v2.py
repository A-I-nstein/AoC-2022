

"""# Day 9"""

with open('input2.txt', 'r') as input:
  rawData = input.read()

def parse(row):
  row = row.split(' ')
  return [row[0], int(row[1])]

movement = list(map(parse, rawData.split('\n')))

class Rope:

  def __init__(self, len):
    self.start = [0, 0]
    self.tailPos = set()
    self.len = len
    
    self.knots = {}
    for knot in range(0, self.len):
      self.knots[knot] = [0, 0]


  def updateRope(self):

    for i in range(1, self.len):

      cur = i
      prev = i - 1

      dx, dy = self.knots[prev][0] - self.knots[cur][0], self.knots[prev][1] - self.knots[cur][1]

      if dx == 0 and dy == 0:
        pass
      

      elif dx == 0:

        if dy == 2:
          self.knots[cur][1] += 1

        if dy == -2:
          self.knots[cur][1] -= 1


      elif dy == 0:

        if dx == 2:
          self.knots[cur][0] += 1

        if dx == -2:
          self.knots[cur][0] -= 1


      else:

        if dx == 2:

          self.knots[cur][0] += 1

          if dy > 0:
            self.knots[cur][1] += 1

          if dy < 0:
            self.knots[cur][1] -= 1


        elif dx == -2:

          self.knots[cur][0] -= 1

          if dy > 0:
            self.knots[cur][1] += 1

          if dy < 0:
            self.knots[cur][1] -= 1
        

        elif dy == 2:

          self.knots[cur][1] += 1

          if dx > 0:
            self.knots[cur][0] += 1

          if dx < 0:
            self.knots[cur][0] -= 1


        elif dy == -2:

          self.knots[cur][1] -= 1

          if dx > 0:
            self.knots[cur][0] += 1

          if dx < 0:
            self.knots[cur][0] -= 1

    self.tailPos.add( str(self.start[0] - self.knots[self.len - 1][0]) + ',' + str(self.start[1] - self.knots[self.len - 1][1]))


  def updateHead(self, dir, steps):

    for _ in range(steps):

      if dir == 'U':
        self.knots[0][0] -= 1

        if self.knots[0][0] < 0:
          self.start[0] += 1

          for i in range(self.len):
            self.knots[i][0] += 1

      elif dir == 'D':
        self.knots[0][0] += 1

      elif dir == 'L':
        self.knots[0][1] -= 1

        if self.knots[0][1] < 0:
          self.start[1] += 1

          for i in range(self.len):
            self.knots[i][1] += 1

      else:
        self.knots[0][1] += 1

      self.updateRope()

"""## Part 1"""

rope = Rope(2)

for step in movement:
  rope.updateHead(step[0], step[1])

print(len(rope.tailPos))

"""##Part 2"""

rope = Rope(10)

for step in movement:
  rope.updateHead(step[0], step[1])

print(len(rope.tailPos))
