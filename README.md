# Lean Up

This tool is intended to help students install & update Lean for CSE 505.

This is the first version of the class we are offering written in Lean,
and the goal of this tool is to make upgrade as seemless as possible for
you over the course of the quarter.

~Note: This is the first iteration of the course with Lean, and this auto-updating software is
a work in progress, if you find issues please report them to us so we can try to improve the
user experince.~

### Setup
Getting set _up_ with _Lean_ takes just a few simple steps.

In order to run `leanup.py` you need a few components:

- [Git](https://git-scm.com/)
- Python 3 (with `pip`), it should be installed on most Linux distributions,
  can easily be installed on macOS with [homebrew](https://brew.sh/), and Windows instructions
  are [here](extras/windows_setup.md).
- [VSCode](https://code.visualstudio.com/)

First clone this tool on to your computer:
```bash
git clone https://github.com/uwplse/leanup
```

Then setup the tool (you should only do this once):

```bash
pip install pipenv
pipenv install
```

You should now be able to run:

```
./leanup.py install
```

![Post Install](/images/post_install.png)

When you are all done you should be able to open the file in `test/example.lean` and see some diagnostics.

![All Done!](/images/all_done.png)

Overall this process should take no more then a few minutes, I tried it on each platform during
the summer, drop by the Slack channel #505-au17 for questions and or help.

### Use

`leanup.py` has a few features ...
