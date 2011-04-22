import ctypes

s = ['c', 'a', 'l', 'i', 'f', 'o', 'r', 'n', 'i', 'a']

s = [ord(x) for x in s]

s += [0x01] + [0x00] * (56 - len(s) - 1)

s += [0x00] * 7 + [0x0A]

M = [s[i+3] + s[i+2]*255 + s[i+1]*(255^2) + s[i]*(255^3)
      for i in range(0,len(s),4)]

A = 0x01234567
B = 0x89abcdef
C = 0xfedcba98
D = 0x76543210

def F(x, y, z):
  return (x & y) | (~x & z)

def G(x, y, z):
  return (x & y) | (x & z) | (y & z)

def H(x, y, z):
  return x ^ y ^ z

def rol(x, n):
  return (x << n) | (x >> (32-n))

# process each 16-work block
for i in range(len(M)/16):
  # copy block i into X
  X = []
  for j in range(16):
    X.append(M[i*16 + j])

  AA = A
  BB = B
  CC = C
  DD = D

  # Round 1
  for i in range(0,16,4):
    A = rol(A + F(B, C, D) + X[i], 3)
    D = rol(D + F(A, B, C) + X[i+1], 7)
    C = rol(C + F(D, A, B) + X[i+2], 11)
    B = rol(B + F(C, D, A) + X[i+3], 19)

  # Round 2
  for i in range(4):
    A = rol(A + G(B, C, D) + X[i] + 0x5A827999, 3)
    D = rol(D + G(A, B, C) + X[i+4] + 0x5A827999, 5)
    C = rol(C + G(D, A, B) + X[i+8] + 0x5A827999, 9)
    B = rol(B + G(C, D, A) + X[i+12] + 0x5A827999, 13)
  
  # Round 3
  for i in (0, 2, 1, 3):
    A = rol(A + H(B, C, D) + X[i] + 0x6ED9EBA1, 3)
    D = rol(D + H(A, B, C) + X[i+8] + 0x6ED9EBA1, 9)
    C = rol(C + H(D, A, B) + X[i+4] + 0x6ED9EBA1, 11)
    B = rol(B + H(C, D, A) + X[i+12] + 0x6ED9EBA1, 15)

  A += AA
  B += BB
  C += CC
  D += DD

print A
print B
print C
print D

