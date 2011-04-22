import os
from Crypto.Hash import MD2

f = open('test.txt', 'wb')
f.write(os.urandom(8192))
f.close()

h = MD2.new()
f = open('test.txt', 'rb')
for i in range(8192/16):
  h.update(f.read(16))
f.close()
print h.hexdigest()

