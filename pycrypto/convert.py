import os, glob
path = ''
for f in glob.glob( os.path.join(path, '*.dia') ):
  print 'dia --export %s.png %s' % (f.split('.')[0], f)
  os.system('dia --export %s.png %s' % (f.split('.')[0], f))
