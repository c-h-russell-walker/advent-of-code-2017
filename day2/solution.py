from argparse import ArgumentParser


def solve_one():
    vals = []

    with open('./day2/input_1.txt') as input_data:
        for line in input_data.readlines():
            line_vals = []
            line = line.strip()
            for val in line.split():
                line_vals.append(int(val))
            vals.append(max(line_vals) - min(line_vals))

    print('Sum of values is: {}'.format(sum(vals)))


def solve_two():
    vals = []

    with open('./day2/input_1.txt') as input_data:
        for line in input_data.readlines():
            line_vals = []
            line = line.strip()
            for val in line.split():
                line_vals.append(int(val))

            line_vals = sorted(line_vals, reverse=True)

            for idx, num in enumerate(line_vals):
                for other in line_vals[idx+1:]:
                    if num % other == 0:
                        vals.append(num/other)
                        break

    print('Sum of values is: {}'.format(sum(vals)))


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
