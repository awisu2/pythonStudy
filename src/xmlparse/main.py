
import os, sys
import xml.etree.ElementTree as ET

# パスから直接パースして取得
def parseFromPath(path):
  tree = ET.parse(path)
  root = tree.getroot()
  return root

# 文字列をパースして取得
def parseFromString(path):
  with open(path) as f:
    str = f.read()
  root = ET.fromstring(str)
  return root

def main():
  args = sys.argv
  if len(args) < 1:
    print('no arg')
    sys.exit()

  path = args[1]

  # root = parseFromPath(path)
  root = parseFromString(path)

  for child in root:
    print(child)

  children = root.findall("child")
  for child in children:
    print(child)

  print(children[0])

  child = root.find("child")
  print(child.tag) # child
  print(child.text) # 
  print(child.get("name")) # foo
  print(child.find("age").text) # foo

if __name__ == '__main__':
  main()
