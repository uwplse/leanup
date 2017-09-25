#! env python3
"""
 __       _______     ___      .__   __.     __    __  .______
|  |     |   ____|   /   \     |  \ |  |    |  |  |  | |   _  \\
|  |     |  |__     /  ^  \    |   \|  |    |  |  |  | |  |_)  |
|  |     |   __|   /  /_\  \   |  . `  |    |  |  |  | |   ___/
|  `----.|  |____ /  _____  \  |  |\   |    |  `--'  | |  |
|_______||_______/__/     \__\ |__| \__|     \______/  | _|.

Usage:
  leanup.py install [PATH]
  leanup.py sync [PATH]

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
from colorama import init, Fore, Style
init()

VERSION = "0.0.1"

WINDOWS_URL  = "https://ci.appveyor.com/api/projects/jroesch/lean/artifacts/build/lean-nightly-windows.zip?branch=master"
LINUX_URL    = "https://github.com/uwplse/lean-nightly/blob/gh-pages/build/lean-nightly-linux.tar.gz?raw=true"
MAC_URL      = "https://github.com/uwplse/lean-nightly/blob/gh-pages/build/lean-nightly-darwin.zip?raw=true"

LEAN_ZIP     = "lean.zip"
LEAN_INSTALL = "lean_install"
LEAN_DL_URL = None

def note(msg):
    print(Fore.YELLOW + "Note:" + msg + Style.RESET_ALL)

def success(msg):
    print(Fore.GREEN + "SUCCESS: " + msg + Style.RESET_ALL)

def detect_platform():
    global LEAN_DL_URL
    sys = platform.system()

    if sys == "Darwin":
        LEAN_DL_URL = MAC_URL
    elif sys == "Windows" or sys.startswith("MSYS_NT"):
        LEAN_DL_URL = WINDOWS_URL
    elif sys == "Linux":
        LEAN_DL_URL = LINUX_URL
    else:
        print("unknown platform: {0}".format(sys))
        exit(0)

def unzip(zip, output):
    call(["unzip", zip])
    nightly = glob.glob("lean-nightly*")
    call(["mv", "-f", nightly[0], LEAN_INSTALL])

def lean_executable_name():
    return "lean"

def clean(path):
    call(["rm", "-r", os.path.join(path, LEAN_ZIP)])

def install(dest_path=None):
    if dest_path is None:
        dest_path = os.getcwd()
    else:
        dest_path = os.path.join(os.getcwd(), dest_path)

    print(dest_path)

    print("Downloading new version of Lean ... ")

    request = requests.get(LEAN_DL_URL)

    with open(os.path.join(dest_path, LEAN_ZIP), 'wb') as f:
        f.write(request.content)

    print ("Unpacking Lean ... ")

    unzip(LEAN_ZIP, "lean_installation")

    lean_path = os.path.join(dest_path, LEAN_INSTALL, "bin", lean_executable_name())
    note("Please set your VSCode lean.executablePath to `{0}`".format(lean_path))
    success("Lean Installed")
    clean(dest_path)

def main(args):
    # Setup Platform specific variables.
    detect_platform()

    if args['install']:
        install(args['PATH'])
    elif args['sync']:
        install(args['PATH'])
    else:
        exit(1)

if __name__ == "__main__":
    arguments = docopt(__doc__, version='leanup {0}'.format(VERSION))
    print(arguments)
    main(arguments)
