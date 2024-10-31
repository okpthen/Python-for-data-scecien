from ft_filter import ft_filter
import sys


def main():
    if len(sys.argv) > 3:
        print("AssertionError: more than two argument are provided")
        exit(0)
    elif len(sys.argv) < 3:
        print("AssertionError: less than two argument are provided")
        exit(0)
    if not sys.argv[2].isdigit():
        print("AssertionError: argument is not an integer")
        exit(0)
    words = sys.argv[1].split(" ")
    num = int(sys.argv[2])
    filter_list = list(ft_filter(lambda x: len(x) > num, words))
    print(filter_list)


if __name__ == "__main__":
    main()
