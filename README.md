# Lean Up

This tool is intended to help students install Lean for CSE 505.

Getting set *up* with Lean takes just a few simple steps.

You need a few components on your computer to install Lean:

    - [Git](https://git-scm.com/)
    - Python 3 (with `pip`), it should be installed on most Linux distros,
      can easily be installed on macOS with [homebrew](), and Windows instructions
      are [here](https://docs.python.org/3/using/windows.html).
    - VSCode (https://code.visualstudio.com/)

First clone this tool on to your computer:
```bash
git clone https://github.com/uwplse/leanup
```

Then setup the tool (you will only need to do this once at the start of the class):

```bash
pip install pipenv
pipenv install
```

You should now be able to run:

```
./leanup.py install
```

When you are all done you should be able to open the file in `test/example.lean` and see some diagnostics.

![All Done!](/images/all_done.png)

Overall this process should take no more then a few minutes, I tried it on each platform during
the summer, drop by the Slack channel #505-au17 for questions and or help.
