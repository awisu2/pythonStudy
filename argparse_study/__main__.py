import argparse

def arg_parse():
  parser = argparse.ArgumentParser(description='this is argparse sample')
  parser.add_argument('nums', metavar='nums', type=int, nargs='+',
                      help='an integer for the accumulator')

  # action: 
  # - store_const: constの値をセットする, 引数がない場合はdefault
  parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

  # dest: parse_args()が返却する際の変数名
  # action: 
  # - store_false: falseをセットする
  # - store_true: trueをセットする
  parser.add_argument('--ping', dest='ping', action='store_true',
                      help='call type ping')

  # action: 
  # - store: 引数の値をセットする
  parser.add_argument('--pinger', dest='pinger', action='store',
                      help='pinger name')

  return parser.parse_args()

def main():
  args = arg_parse()

  print(f'nums {args.nums}, accumulate: {args.accumulate(args.nums)}')
  if args.ping:
    print(f"pong {args.pinger}")

if __name__ == "__main__":
  main()