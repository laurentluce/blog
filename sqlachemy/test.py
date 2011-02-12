delta = 0
def gmm():
  global delta
  delta0 = delta
  delta += 1
  return delta0

print gmm()
print gmm()

def gmm2():
  delta0 = gmm2.delta
  gmm2.delta += 1
  return delta0

gmm2.delta = 0
print gmm2()
print gmm2()

class Example:
  def __init__(self):
    self.delta = 0
  def gmm(self):
    delta0 = self.delta
    self.delta += 1
    return delta0

o = Example()
print o.gmm()
print o.gmm()

def gmm3():
  delta = 0
  while True:
    delta0 = delta
    delta += 1
    yield delta0

for i in gmm3():
  print i

