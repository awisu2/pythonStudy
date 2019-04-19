from __init__ import Base, Sub, SubNoInit

def main():
  print('-- base --')
  base = Base('base')
  print(base.name, base.pubname)

  base.name = 'change name base'
  base.__name = 'change name ggggg' # エラーにはならないが値の変更は起きない
  base.pubname = 'change pubname base'
  print(base.name, base.pubname)

  print('-- sub --')
  sub = Sub('sub', 'sub-base')
  print(sub.name, sub.subname())

  print('-- sub no init --')
  sub_no_init = SubNoInit('sub no init')
  print(sub_no_init.name)

if __name__ == "__main__":
  main()