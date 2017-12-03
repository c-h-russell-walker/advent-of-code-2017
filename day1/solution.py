from argparse import ArgumentParser


def _get_input():
    with open('./day1/input_1.txt') as input_data:
        data = input_data.read().strip()
    return data


def solve_one():
    data = _get_input()

    vals = []

    last_val = data[-1:]

    for val in data:
        if val == last_val:
            vals.append(int(last_val))
        last_val = val

    print('Sum of values is: {}'.format(sum(vals)))


def solve_two():
    data = _get_input()
    data_len = len(data)
    half_val = data_len / 2

    vals = []

    for idx, val in enumerate(data):
        next_idx = (half_val + idx) % data_len
        compare_val = data[next_idx:next_idx + 1]

        if val == compare_val:
            vals.append(int(compare_val))

        last_val = val

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
