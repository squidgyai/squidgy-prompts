from tests.runner import *
import argparse

# run tests when executed
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Squidgy Prompts Test Runner.')

    #training arguments
    parser.add_argument('--file', type=str, required=False)
    parser.add_argument('--test', type=str, required=False)

    args = parser.parse_args()

    run_tests(args.file, args.test)