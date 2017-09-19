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
from subprocess import call
import os
import platform
import requests

VERSION = "0.0.1"

WINDOWS_URL  = "https://ci.appveyor.com/api/projects/jroesch/lean/artifacts/build/lean-nightly-windows.zip?branch=master"
LINUX_URL    = "https://github.com/uwplse/lean-nightly/blob/gh-pages/build/lean-nightly-linux.tar.gz?raw=true"
MAC_URL      = "https://github.com/uwplse/lean-nightly/blob/gh-pages/build/lean-nightly-darwin.zip?raw=true"

LEAN_ZIP     = "lean.zip"
LEAN_INSTALL = "lean_install"

def unzip(zip, output):
    call(["unzip", zip])
    call(["mv", LEAN_ZIP, LEAN_INSTALL])

def main(args):
    print("Hello!")
    sys = platform.system()

    url = None
    if sys == "Darwin":
        url = MAC_URL
    elif sys == "Windows":
        url = WINDOWS_URL
    elif sys == "Linux":
        url = LINUX_URL
    else:
        print("unknown platform: {0}".format(sys))
        exit(0)

    request = requests.get(url)

    with open(LEAN_ZIP, 'wb') as f:
        f.write(request.content)

    unzip(LEAN_ZIP, "lean_installation")

    lean_path = os.path.join(os.getcwd(), LEAN)

    print("Please set your VSCode path: {0}".format(lean_path))

    print("installed")


if __name__ == "__main__":
    arguments = docopt(__doc__, version='leanup {0}'.format(VERSION))
    print(arguments)
    main(arguments)
