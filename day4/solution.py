from argparse import ArgumentParser
from collections import Counter

def solve(second=None):
    valid_count = 0
    with open('./day4/input_1.txt') as input_data:
        for line in input_data.readlines():
            ctr = Counter()
            for word in line.split():
                if second:
                    word = ''.join(sorted(word))
                ctr[word] += 1
            most_common = ctr.most_common(1)[0]
            if most_common[1] == 1:
                valid_count +=1

    print('Number of valid pass phrases: {}'.format(valid_count))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--second',
        action='store_true',
        help='Pass in order to run second version.'
    )
    args = parser.parse_args()

    solve(second=args.second)
