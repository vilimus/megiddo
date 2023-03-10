import numpy as np

class Megiddo():
  def __init__(self):
    self.board = np.zeros((6,6), dtype=int)
    self.turn = 0
    self.won = [False, False]

  def __repr__(self):
    D = dict(zip(range(-1,2),"o.x"))
    return "\n".join([" ".join(x) for x in np.vectorize(lambda x: D[x])(self.board)]) + f"\n{D[1-2*(self.turn%2)]} to move."
    
  def get(self, i: int, j: int):
    return self.board[i%6, j%6]

  def set(self, i: int, j: int, x: int):
    self.board[i%6, j%6] = x

  def move(self, i: int, j: int):

    if self.get(i,j) != 0:
      return
    
    self.set(i, j, (-1)**(self.turn%2))
    self.turn += 1

    # capture
    x = self.get(i,j)
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
      a,b,c = [self.get(i+k*di,j+k*dj) for k in range(1,4)]
      if a==b==-x and c==x:
        self.set(i+di,j+dj,x)
        self.set(i+2*di,j+2*dj,x)

    # win condition
    for i in range(6):
      for di,dj in [(1,0),(0,1),(1,1),(1,-1)]:
        x = [self.get(i+k*di,j+k*dj) for k in range(6)]
        s = sum(x)
        if s==6:
          self.won[0] = True
        elif s==-6:
          self.won[1] = True
