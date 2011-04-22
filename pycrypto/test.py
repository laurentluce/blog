import os
import timeit

CHUNK_SIZE = 65536
NB_CHUNKS = 16

f = open('test.txt', 'wb')
for i in range(NB_CHUNKS):
  f.write(os.urandom(CHUNK_SIZE))
f.close()

t = timeit.Timer('ripemd160.test(%d, %d)' % (NB_CHUNKS, CHUNK_SIZE), 'import ripemd160')

print min(t.repeat(3, 1000))
