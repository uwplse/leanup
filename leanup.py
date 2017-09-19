#! env python3
"""
 __       _______     ___      .__   __.     __    __  .______
|  |     |   ____|   /   \     |  \ |  |    |  |  |  | |   _  \\
|  |     |  |__     /  ^  \    |   \|  |    |  |  |  | |  |_)  |
|  |     |   __|   /  /_\  \   |  . `  |    |  |  |  | |   ___/
|  `----.|  |____ /  _____  \  |  |\   |    |  `--'  | |  |
|_______||_______/__/     \__\ |__| \__|     \______/  | _|.

Usage:
  leanup.py install

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt

VERSION = "0.0.1"

def main(args):
    print("Hello!")

if __name__ == "__main__":
    arguments = docopt(__doc__, version='leanup {0}'.format(VERSION))
    print(arguments)
    main(arguments)
