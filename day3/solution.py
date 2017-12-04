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


def _get_left_direction(direction):
    # Possible values:
    right = (1, 0)
    up = (0, -1)
    left = (-1, 0)
    down = (0, 1)

    if direction == right:
        return up
    elif direction == up:
        return left
    elif direction == left:
        return down
    elif direction == down:
        return right


def _turn_left(coords, direction):
    return (
        coords[0] + direction[0],
        coords[1] + direction[1]
    )


def _get_surrounding_sum(matrix, coords):
    total = 0
    x_start = coords[0] - 1
    y_start = coords[1] - 1
    for x in range(x_start, x_start + 3):
        for y in range(y_start, y_start + 3):
            if matrix[x][y] is not None:
                total += matrix[x][y]

    return total


def solve_two():
    puzz_input = 289326

    matrix_width = None

    # Using `puzz_input` as arbitrary ceiling in case of error
    # - prevents infinite loop
    for i in range(1, puzz_input):
        if i * i > puzz_input:
            matrix_width = i
            break

    matrix = [
        [None for x in range(matrix_width)]
        for y in range(matrix_width)
    ]

    # Figure out what the value of the center is
    center = (int(matrix_width / 2), int(matrix_width / 2))

    # Init first value
    matrix[center[0]][center[1]] = 1

    # Init coordinates to one square right of center
    second_square = (center[0], center[1] + 1)
    prev_coords = second_square
    matrix[second_square[0]][second_square[1]] = 1

    # Start hedaing `RIGHT` (incrementing x-axis)
    direction = (1, 0)

    for i in range(1, puzz_input):
        # Calculate what new direction would be
        left_turn = _get_left_direction(direction)

        # Try and turn left & if cannot move forward
        # Calculate what left turn value would be
        new_coords = _turn_left(prev_coords, left_turn)

        if matrix[new_coords[0]][new_coords[1]] is None:
            direction = left_turn
        else:
            # Forward direction
            new_coords = (
                prev_coords[0] + direction[0],
                prev_coords[1] + direction[1]
            )

        new_val = _get_surrounding_sum(matrix, new_coords)

        matrix[new_coords[0]][new_coords[1]] = new_val

        prev_coords = new_coords

        if new_val > puzz_input:
            print('Value found greater than input: {}'.format(new_val))
            break


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
