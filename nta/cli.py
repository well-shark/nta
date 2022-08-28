import sys
import argparse


def main(*argv):
    if not argv:
        argv = list(sys.argv)

    parser = argparse.ArgumentParser()

    # input_parser = parser.add_mutually_exclusive_group()
    parser.add_argument('-a', '--show-all', action='store_true',
                        help='Display all gpu properties above')


if __name__ == '__main__':
    main(*sys.argv)
