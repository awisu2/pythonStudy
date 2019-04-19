import re

# re.match 先頭からの一致
# re.search 概ね想定通りの動作

def try_search(str, res, flag=0):
  print(f'----- try_search: {str} -----')
  for _re in res:
    print(f'-- STR: {str}, RE: {_re}')
    match = re.search(_re, str, flag)
    if match:
      print(match, match.lastindex, match.string, match.group(0))
      for group in match.groups():
        print('group', group)

    else:
      print('no hit')

def search_lasts(s, pattern, *, ignore_front=False):
  """
  特定のパターンが後方に複数存在するときに
  複数のマッチオブジェクトを取得して返却する

  note:
  reの関数では、r'(anystring)+'を指定したとき
  最後の1つのみのマッチオブジェクトを取得するため

  ex:
  s = abcde[f][g], pattern = r'\[[^\[\]]+\]' とすることで
  [f], [g]2つのマッチオブジェクトを返却
  """
  pos = 1 if ignore_front else 0

  # 一度後方一致で文字列を抽出
  re_item = re.compile(pattern)
  re_items = re.compile(r'(' + pattern + r')+$')
  m = re_items.search(s, pos=pos)
  if not m:
    return None, None

  # 個別に一致
  ms = re_item.finditer(s, pos=m.start(), endpos=m.end())
  if not ms:
    return None, None

  return ms, m

def try_findall(str, res):
  print(f'----- try_findall: {str} -----')
  for _re in res:
    print(f'-- STR: {str}, RE: {_re}')
    print(re.findall(_re, str))

def try_finditer(str, res):
  print(f'----- try_finditer: {str} -----')
  for _re in res:
    print(f'-- STR: {str}, RE: {_re}')
    iter = re.finditer(_re, str)
    for item in iter:
      print(item)

if __name__ == "__main__":
  strs = [
    '[a]hogehoge[b][c][d]',
    '[a][b][c][d]',
    '[a]hogehoge',
    '[[a]]hogehoge[[[b]]]',
  ]

  res = [
    # r'^\[.*\]',
    # r'^\[.*?\]', # *?は最短一致
    # r'(?<=\[).*?(?=\])', # 肯定先読み、戻り読み
    # r'\[.*?\]',


    # r'((?<=\[).*?(?=\]))+$', # 肯定先読み、戻り読み
    # r'\[.*?\]$',

    # r'\[[^\[\]]+\]', # [[a]]といった重複しているものに対応

    # 囲い文字を除外
    # r'\[([^\[\]]+)\]',
    # r'(?<=\[)[^\[\]]+(?=\])',

    # 後方に存在するものを抽出
    # r'\[([^\[\]]+)\]$',

    # 後方に存在するものを複数抽出
    # r'(\[([^\[\]]+)\])+$',
    r'(\[[^\[\]]+\])+$', # グループを複数指定した場合、最後の1つだけがヒットする
    r'((\[[^\[\]]+\])+)$', # グループを複数指定した場合、最後の1つだけがヒットする
  ]

  # for s in strs:
  #   try_search(s, res)

  # for s in strs:
  #   try_findall(s, res)

  # for s in strs:
  #   try_finditer(s, res)

  for s in strs:
    print(f'----- search_lasts {s}')
    # ms = search_lasts(s, r'\[[^\[\]]+\]', ignore_front=True)
    # if ms:
    #   for m in ms:
    #     print(m)

    ms, m = search_lasts(s, r'\[[^\[\]]+\]', ignore_front=True)
    if ms:
      print(m)
      for m in ms:
        print(m, m.group(0), m.group(0)[1:-1])
