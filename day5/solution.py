from argparse import ArgumentParser


def solve_one(second=None):
    ctr = 0
    vals = []
    with open('./day5/input_1.txt') as input_data:
        for line in input_data.readlines():
            vals.append(int(line.strip()))

    curr_index = 0

    try:
        while True:
            old_index = curr_index
            curr_index = curr_index + vals[curr_index]
            vals[old_index] += 1
            ctr += 1
    except IndexError:
        print('Number of jumps to escape maze: {}'.format(ctr))


def solve_two():
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--second',
        action='store_true',
        help='Pass in order to run second version.'
    )
    args = parser.parse_args()

    if not args.second:
        solve_one()
    else:
        solve_two()
