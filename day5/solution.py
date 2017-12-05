from argparse import ArgumentParser


def solve(second=None):
    ctr = 0
    vals = []
    with open('./day5/input_1.txt') as input_data:
        for line in input_data.readlines():
            vals.append(int(line.strip()))

    curr_index = 0

    while curr_index < len(vals):
        offset = vals[curr_index]
        if second and offset >= 3:
            vals[curr_index] -= 1
        else:
            vals[curr_index] += 1
        curr_index += offset
        ctr += 1
    print('Number of jumps to escape maze: {}'.format(ctr))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--second',
        action='store_true',
        help='Pass in order to run second version.'
    )
    args = parser.parse_args()

    solve(args.second)
