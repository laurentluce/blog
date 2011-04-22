from Crypto.Hash import RIPEMD160

def test(nb_chunks, chunk_size):
  h = RIPEMD160.new()
  f = open('test.txt', 'rb')
  for i in range(nb_chunks):
    h.update(f.read(chunk_size))
  f.close()
  d = h.hexdigest()
