# -*- coding: utf-8 -*-

# for cli function
def main(args):
    print('run ' + __file__)
    print('hello ' + args.name)
    for val in args.vals:
        print('var:'+ value)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='this is base of python script')

    # args
    parser.add_argument('vals', metavar='any', type=str, nargs='*', help='any vlues')

    # option params
    parser.add_argument('-name', action='store', default='world', help='hello <name>')

    main(parser.parse_args())
