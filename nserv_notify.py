#!/usr/bin/env python
"""
Command-line tool for posting notifications
"""
import argparse

from nserv import notify


def parse_args():
    parser = argparse.ArgumentParser(
       description='Post a notification.'
    )
    parser.add_argument('-m', '--message', required=True)
    parser.add_argument('-l', '--level',
                        choices=['success', 'info', 'warning', 'danger'],
                        required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    notify(args.message, args.level)
