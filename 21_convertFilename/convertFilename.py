# -*- coding: utf-8 -*-
import os.path
import re
import shutil

def list(dirname, pattern, repl, options):
  # create pattern
  _pattern = re.compile(r'{0}'.format(pattern))

  # walk
  count=0
  for _, _, filenames in os.walk(dirname):
    for filename in filenames:
      convert = re.sub(_pattern, repl, filename)
      if(filename == convert):
        continue

      count += 1
      if(options["num"] != 0 and count > options["num"]):
        break

      src = dirname + "/" + filename
      dist = dirname + "/" + convert
      print(src + ' > ' + dist)

      if options["dryrun"]:
        if options["v"]:
          print("dryrun::not convert")
        continue

      # move
      if options["v"]:
        print("move!")
      shutil.move(src, dist)

# for cli function
def main(args):
  if not os.path.isdir(args.base):
    print("base is not directory")
    return

  # get options
  options = {
    "dryrun": args.dryrun,
    "num": args.num,
    "v": args.v
  }

  # system echo
  if(options["v"]):
    print("args:", args)
    print("options:", options)

  if(options["dryrun"]):
    print('dryrun')

  # run
  list(args.base, args.pattern, args.repl, options)

if __name__ == '__main__':
  import argparse
  name, _ = os.path.splitext(__file__)
  parser = argparse.ArgumentParser(description='I am '+name)

  # args
  parser.add_argument('vals', metavar='any', type=str, nargs='*', help='any vlues')

  # option params
  parser.add_argument('--base', action='store', default='.', help='base dirctory(default current diirectory)')
  parser.add_argument('--pattern', action='store', required=True, help='much pattern')
  parser.add_argument('--repl', action='store', required=True, help='replace pattern')
  parser.add_argument('--dryrun', action='store_true', help='dryrun')
  parser.add_argument('--num', action='store', type=int, default=0, help='number of convert')
  parser.add_argument('-v', action='store_true', help='vervose')

  main(parser.parse_args())
