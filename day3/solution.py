from argparse import ArgumentParser


def _manhattan_distance(point_a, point_b):
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def solve_one():
    puzz_input = 289326

    size = None
    matrix_width = None

    # Using `puzz_input` as arbitrary ceiling in case of error
    # - prevents infinite loop
    for i in range(1, puzz_input):
        if i * i > puzz_input:
            size = i * i
            matrix_width = i
            break

    input_diff = size - puzz_input

    if input_diff > matrix_width:
        # TODO - account for value wrapping to the right hand col. etc.
        raise NotImplementedError('Account for the diff coordinate vals!')

    # Be sure to add one
    input_coords = (0, input_diff + 1)

    # Figure out the value of the center is
    center = (matrix_width / 2, matrix_width / 2)

    print(
        'Distance from center: {}'.format(
            _manhattan_distance(center, input_coords)
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
