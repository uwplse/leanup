# Lean Up

This tool is intended to help students install & update Lean for CSE 505.

This is the first version of the class we are offering written in Lean,
and the goal of this tool is to make upgrade as seemless as possible for
you over the course of the quarter.

_Note: This is the first iteration of the course with Lean, and this auto-updating software is
a work in progress, if you find issues please report them to us so we can try to improve the
user experince._

### Setup
Getting set _up_ with _Lean_ takes just a few simple steps.

In order to run `leanup.py` you need a few components:

- [Git](https://git-scm.com/)
- Python 3 (with `pip`), it should be installed on most Linux distributions,
  can easily be installed on macOS with [homebrew](https://brew.sh/), and Windows instructions
  are [here](docs/windows_setup.md).
- [VSCode](https://code.visualstudio.com/)

First clone this tool on to your computer:
```bash
git clone https://github.com/uwplse/leanup
```

Then setup the tool (you should only do this once):

```bash
pip install pipenv
cd leanup
pipenv install
pipenv shell
```

You should now be able to run:

```
./leanup.py install
```

![Post Install](/images/post_install.png)

Now copy the path provided to you by the tool since we will need it for VSCode.
First open the `User Settings` window of VSCode (`cmd-,` or `ctrl-,` depending on platform),
and modify the `lean.executablePath` to point to the executable provided by `leanup`.

![User Settings](/images/settings.png)

When you are all done you should be able to open the file in `test/example.lean` and see some diagnostics.

![All Done!](/images/all_done.png)

Overall this process should take no more then a few minutes. I've done my best to test it on the major
platforms, if you have trouble please drop by the Slack channel `#505-au17` for questions/help.

### Use

`leanup.py` has a few features ...
