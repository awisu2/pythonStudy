# -*- coding: utf-8 -*-
# 16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー — Python 3.6.1 ドキュメント 
# https://docs.python.jp/3/library/argparse.html#argparse.ArgumentParser.add_argumentimport argparse
import argparse

def length(v):
    return 'call length ' + str(len(v))

def main(args):
    print('foo:' + str(args.foo))
    print('strs:' + str(args.strs))
    print('nums:' + str(args.nums))
    print('v:' + str(args.v))
    print(args.dest1(args.nums))
    print(args)

if __name__ == '__main__':
    # STEP1: make parser(add -h,--help automaticaly)
    parser = argparse.ArgumentParser(description='argparse test.')
    # STEP2: args settings
    # add_argument
    # first: option or simple parameter(--foo or bar)
    # metavar: help information name
    # type: parameter type(ex:int)
    # nargs: arg nums(ex: 1,+,? )
    # dest: function name in args
    parser.add_argument('nums', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    # nargsを指定しない場合スカラ値、指定した場合それがnargs=1だとしてもListになる
    parser.add_argument('strs', metavar='S', type=str,
                        help='string for the accumulator')
    # option params
    parser.add_argument('--foo', nargs='?', const='set foo',
                        default='not set foo', help='any params')
    parser.add_argument('-v', action='store_true', help='print detail')

    # function
    # 特定のオプションがあったときの挙動を変更したいときなどに有効
    parser.add_argument('--length', dest='dest1', action='store_const',
                        const=length, default=sum,
                        help='length the nums (default: find the sum)')
    main(parser.parse_args())

# usage: argparseSample.py [-h] [--foo [FOO]] [--length] N [N ...] S
#
# argparse test.
#
# positional arguments:
#   N            an integer for the accumulator
#   S            string for the accumulator
#
# optional arguments:
#   -h, --help   show this help message and exit
#   --foo [FOO]  any params
#   --length     length the nums (default: find the sum)

