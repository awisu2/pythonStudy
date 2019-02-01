import os

def split_sample(path):
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

def listdir_sample():
  # ファイル、ディレクトリを関係なく取得
  dir = r'..\\'
  print('listdir', os.listdir(dir))

  print('listdir1:', listdir(dir))
  print('listdir2:', listdir(dir))
  print('listdir(only_file): ', listdir(dir, is_dir=False, is_file=True))
  print('listdir(only_dir): ', listdir(dir, is_dir=True, is_file=False))
  print('listdir(only_file, recursive): ', listdir(dir, is_dir=False, is_file=True, is_recursive=True))
  print('listdir(only_dir, recursive): ', listdir(dir, is_dir=True, is_file=False, is_recursive=True))

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

def listdir(dir, *, is_dir=True, is_file=True, is_recursive=False):
  """
  windowsだとglobがうまく動かないことがあるので,
  listdirの使い勝手を少し良くしてみる
  """
  files = os.listdir(dir)
  if is_dir and is_file and not is_recursive:
    return files

  _files = []
  for file in files:
    path = os.path.join(dir, file)
    if os.path.isdir(path):
      if is_dir:
        _files.append(path)

      if is_recursive:
        __files = listdir(path, is_dir=is_dir, is_file=is_file, is_recursive=is_recursive)
        for _file in __files:
          _files.append(_file)

    elif os.path.isfile(path):
      if is_file:
        _files.append(path)

  return _files

strs = (
  r'c:\a\b\abc.txt',
  r'\a\b\abc.txt',
  r'\a\b\\',
  r'abc.txt',
  r'a\b\abc.txt',
  r'E:\develop\study'
)

for s in strs:
  split_sample(s)
  print('-----------', s)

listdir_sample()
print('-----------')
