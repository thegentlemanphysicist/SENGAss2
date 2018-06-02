#!/usr/bin/env python3

import fileinput
import sys


def main():
    for line in fileinput.input():
        print(line)


if __name__ == '__main__':
    main()