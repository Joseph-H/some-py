import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    # required argument
    # you can have the long argument as well, just put it after the short argument and use two dashes ie --execute
    parser.add_argument('-x', '--execute',  action="store", required=True,
                        help='Help text for option X')

    # optional arguments
    # if you have two arguments that can be used together; they're mutually exclusive, use a mutually exclusive group
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-y', help='Help text for option Y', default=False)
    group.add_argument('-z', help='Help text for option Z', type=int)

    print(parser.parse_args())

if __name__ == '__main__':
    get_args()
