class Base(object):
  # "__"をつけるとプライベート
  __name = ''
  pubname = ''

  @classmethod
  def create(cls, name):
    return cls(name)

  def __init__(self, name):
    print(f'__name: {self.__name}, pubname: {self.pubname}')

    self.__name = name
    # テストのため、pub_をつけてセット
    self.pubname = 'pub_' + name

    print(f'__name: {self.__name}, pubname: {self.pubname}')

  def name(self):
    return self.__name

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
  print(base.name())

  print('-- sub --')
  sub = Sub('sub', 'sub-base')
  print(sub.name(), sub.subname())

  print('-- sub no init --')
  SubNoInit('sub no init')

if __name__ == "__main__":
  main()