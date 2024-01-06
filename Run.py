import getopt
import importlib
import sys


def main(argv):
    args, opts = getopt.getopt(argv, 'p:d:y', ['puzzle=', 'day=', 'year='])
    puzzle = args[0][1]
    day = args[1][1]
    year = args[2][1]
    aoc = importlib.import_module(f"y{year}.day{day}.puzzle{puzzle}")
    base_path = f"./y{year}/day{day}"
    print(f"Running Advent of Code {year} Day {day} Puzzle {puzzle}")
    aoc.run(base_path)


main(sys.argv[1:])
