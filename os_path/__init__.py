import os.path

def test(path):
  # windowsでのドライブが存在するとき、ドライブ名とその他を分割する
  print('splitdrive: ', os.path.splitdrive(path))
  # ディレクトリとテキストを分割する
  print('split: ', os.path.split(path))
  print('splitext: ', os.path.splitext(path))

  print('join: ', os.path.join(path, '_join1', '_join2'))
  print('basename: ', os.path.basename(path))
  print('isfile: ', os.path.isfile(path))
  print('isdir: ', os.path.isdir(path))
  print('splitdetail', path_splitdetail(path))

def path_splitdetail(path):
  """
  pathをdrive, directory, name, extに分割
  """
  st = os.path.splitdrive(path)
  drive = st[0]

  st = os.path.split(st[1])
  directory = st[0]

  st = os.path.splitext(st[1])
  name = st[0]
  ext = st[1]

  return {
    'drive': drive,
    'directory': directory,
    'name': name,
    'ext': ext
  }

strs = (
  r'c:\a\b\abc.txt',
  r'\a\b\abc.txt',
  r'\a\b\\',
  r'abc.txt',
  r'a\b\abc.txt',
  r'E:\develop\study'
)

for s in strs:
  print('-----------', s)
  test(s)

