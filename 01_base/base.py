# -*- coding: utf-8 -*-
import os.path

# for cli function
def main(args):
    print('run ' + __file__)
    print('hello ' + args.name)
    for val in args.vals:
        print('var:'+ value)

if __name__ == '__main__':
    import argparse
    name, _ = os.path.splitext(__file__)
    parser = argparse.ArgumentParser(description='I am '+name)

    # args
    parser.add_argument('vals', metavar='any', type=str, nargs='*', help='any vlues')

    # option params
    parser.add_argument('-name', action='store', default='world', help='hello <name>')

    main(parser.parse_args())
