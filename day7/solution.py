from argparse import ArgumentParser

def solve_one():
    parents_set = set()
    children_set = set()
    with open('./day7/input_1.txt') as input_data:
        for line in input_data.readlines():
            line = line.strip()
            parts = line.strip().split()
            program_name = parts[0]
            weight = parts[1].strip('()')

            parents_set.add(program_name)

            if len(parts) > 2:
                assert parts[2] == '->', 'Delimiter missing?!'
                children = [p.strip(',') for p in parts[3:]]
                for child in children:
                    children_set.add(child)

    print(
        'Root node/program: {}'.format(
            parents_set.difference(children_set)
        )
    )


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
