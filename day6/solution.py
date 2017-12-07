from argparse import ArgumentParser


def solve(second=None):
    memory_banks = [
        11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11
    ]

    history = []

    solved = False
    first_occurrence = None
    second_occurrence = None

    while not solved:
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

        if not second:
            if memory_banks in history:
                solved = True
        else:
            if memory_banks in history and first_occurrence is None:
                first_occurrence = len(history)
                history = []
                memory_banks[first_occurrence:]
            elif memory_banks in history and second_occurrence is None:
                second_occurrence = len(history)
                solved = True

    if not second:
        print('Answer: {}'.format(len(history)))
    else:
        print('Answer: {}'.format(second_occurrence))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--second',
        action='store_true',
        help='Pass in order to run second version.'
    )
    args = parser.parse_args()

    solve(second=args.second)
