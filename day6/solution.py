from argparse import ArgumentParser


def solve(second=None):
    memory_banks = [
        11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11
    ]

    history = []

    while memory_banks not in history:
        history.append(memory_banks[:])
        max_val = max(memory_banks)
        index = memory_banks.index(max_val)

        dist_val = memory_banks[index]
        memory_banks[index] = 0
        while dist_val:
            index += 1
            if index >= len(memory_banks):
                index = 0
            memory_banks[index] += 1
            dist_val -= 1

    print('Answer: {}'.format(len(history)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--second',
        action='store_true',
        help='Pass in order to run second version.'
    )
    args = parser.parse_args()

    solve(second=args.second)
