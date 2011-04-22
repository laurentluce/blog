from Crypto.Hash import MD4

def test(nb_chunks, chunk_size):
  h = MD4.new()
  f = open('test.txt', 'rb')
  for i in range(nb_chunks):
    h.update(f.read(chunk_size))
  f.close()
  d = h.hexdigest()
