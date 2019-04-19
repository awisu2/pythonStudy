from __init__ import Base, Sub, SubNoInit

def main():
  print('-- base --')
  base = Base('base')
  print(f'get class property:: name: {base.name}, pubname: {base.pubname}')

  base.name = 'change name base'
  base.__name = 'change name nochange' # エラーにはならないが値の変更は起きない
  base.pubname = 'change pubname base'
  base.y
  print(f'get class property after set:: name: {base.name}, pubname: {base.pubname}, x: {base.x}, y: {base.y}')

  print('-- sub --')
  sub = Sub('sub', 'sub-base')
  print(f'get class property:: name: {sub.name}, subname: {sub.subname}')

  print('-- sub no init --')
  sub_no_init = SubNoInit('sub no init')
  print(f'get class property:: name: {sub_no_init.name}')

if __name__ == "__main__":
  main()