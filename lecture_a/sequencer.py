import argparse
from math import sqrt

# Sequence generators
def gen_fibonacci_sequence(length):
    if length == 1:
        return [0]
    if length == 2:
        return [0, 1]
    
    sequence = [0, 1]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:length]

def gen_prime_sequence(length):
    def is_prime(y):
        if y < 2:
            return False
        for i in range(2, int(sqrt(y)) + 1):
            if y % i == 0:
                return False
        return True

    sequence = []
    x = 2
    while len(sequence) < length:
        if is_prime(x):
            sequence.append(x)
        x += 1
    return sequence

def gen_square_sequence(length):
    return [i**2 for i in range(1, length + 1)]

def gen_triangular_sequence(length):
    return [i*(i+1)/2 for i in range(1, length + 1)]

def gen_factorial_sequence(length):
    z = 1
    seq = [1]
    for i in range(2, length+1):
        z *= i
        seq.append(z)
    return seq

def argparser():
    parser = argparse.ArgumentParser(description='Sequence generator')
    parser.add_argument('--length', type=int, help='Sequence length', required=True)
    parser.add_argument('--sequence', choices=['fibonacci', 'prime', 'square', 'triangular', 'factorial'],
                        help='Sequence type', required=True)

    args = parser.parse_args()
    return args

def main(args):
    if args.length == 0:
        return []
    match args.sequence:
        case 'fibonacci':
            result = gen_fibonacci_sequence(args.length)
        case 'prime':
            result = gen_prime_sequence(args.length)

        case 'square':
            result = gen_square_sequence(args.length)

        case 'triangular':
            result = gen_triangular_sequence(args.length)

        case 'factorial':
            result = gen_factorial_sequence(args.length)
    # Argparser handles the case if sequence is not one of the above
    return result

if __name__ == '__main__':
    args = argparser()
    result = main(args)
    print(f"The {args.sequence} sequence of length {args.length} is: {result}")