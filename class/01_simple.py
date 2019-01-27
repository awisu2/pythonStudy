class Base(object):
  # 普通に記述するとパブリックアクセス可能なプロパティ
  pubname = ''

  # "__"をつけるとプライベート
  __name = ''

  @classmethod
  def create(cls, name):
    return cls(name)

  def __init__(self, name):
    print(f'check property already set: {self.__name}, {self.pubname}')

    self.__name = name
    # テストのため、pub_をつけてセット
    self.pubname = 'pub_' + name

  # いわゆるgetter
  @property
  def name(self):
    return self.__name

  # いわゆるsetter
  @name.setter
  def name(self, name):
    self.__name = name

class Sub(Base):
  def __init__(self, subname, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__subname = subname

  def subname(self):
    return self.__subname

class SubNoInit(Base):
  pass

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