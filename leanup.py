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
import glob

VERSION = "0.0.1"

WINDOWS_URL  = "https://ci.appveyor.com/api/projects/jroesch/lean/artifacts/build/lean-nightly-windows.zip?branch=master"
LINUX_URL    = "https://github.com/uwplse/lean-nightly/blob/gh-pages/build/lean-nightly-linux.tar.gz?raw=true"
MAC_URL      = "https://github.com/uwplse/lean-nightly/blob/gh-pages/build/lean-nightly-darwin.zip?raw=true"

LEAN_ZIP     = "lean.zip"
LEAN_INSTALL = "lean_install"

user_platform = None
def detect_platform():
    sys = platform.system()

    if sys == "Darwin":
        user_platform = MAC_URL
    elif sys == "Windows":
        user_platform = WINDOWS_URL
    elif sys == "Linux":
        user_platform = LINUX_URL
    else:
        print("unknown platform: {0}".format(sys))
        exit(0)

def unzip(zip, output):
    call(["unzip", zip])
    nightly = glob.glob("lean-nightly*")
    call(["mv", nightly[0], LEAN_INSTALL])

def lean_executable_name():
    return "lean"

def main(args):
    detect_platform()

    print("Downloading new version of Lean ... ")

    request = requests.get(url)

    with open(LEAN_ZIP, 'wb') as f:
        f.write(request.content)

    print ("Unpacking Lean ... ")

    unzip(LEAN_ZIP, "lean_installation")

    lean_path = os.path.join(os.getcwd(), LEAN_INSTALL, "bin", lean_executable_name())

    print("Note: Please set your VSCode lean.executablePath to `{0}`".format(lean_path))

    print("Lean Sucessfully Installed.")

if __name__ == "__main__":
    arguments = docopt(__doc__, version='leanup {0}'.format(VERSION))
    print(arguments)
    main(arguments)
