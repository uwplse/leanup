# Lean Up

This tool is intended to help students install & update Lean for CSE 505.

This is the first version of the class we are offering written in Lean,
and the goal of this tool is to make upgrade as seamless as possible for
you over the course of the quarter.

_Note: This is the first iteration of the course with Lean, and this auto-updating software is
a work in progress, if you find issues please report them to us so we can try to improve the
user experince._

## Setup
Getting set _up_ with _Lean_ takes just a few simple steps.

In order to run `leanup.py` you need a few components:

- [Git](https://git-scm.com/)
- Python 3 (with `pip`), it should be installed on most Linux distributions,
  can easily be installed on macOS with [homebrew](https://brew.sh/), and Windows instructions
  are [here](docs/windows_setup.md).
- [VSCode](https://code.visualstudio.com/)
- [GMP](https://gmplib.org/) (should be installed on MSYS2 or Linux, can be installed with Homebrew)

First clone this tool on to your computer:
```bash
git clone https://github.com/uwplse/leanup
```

Then setup the tool (you should only do this once: *please substitute `3.XX` for your Python 3 version*).

```bash
pip install pipenv
cd leanup
pipenv --python 3.XX install
pipenv shell
```

You should now be able to run:

```
./leanup.py install
```

You should be looking at something like this:
![Post Install](/images/post_install.png)
Make a note of the `lean.executablePath`; you'll need it in a second.

### Install Lean mode for VSCode
You can either:

* Install from the VSCode website: [Lean mode](https://marketplace.visualstudio.com/items?itemName=jroesch.lean). When you click on the green "Install" button on that page, it should open VSCode and install the plugin.
* Install from the editor: open the command palette (`cmd-shift-p` or `ctrl-shift-p`) and select `Extensions: Install Extensions`. You should be presented with a panel in the gutter, where you can type Lean, and click install.

![Extension Install](images/ext_window.png)

You can check that the extension has been successfully installed by opening up the Extensions gutter (`cmd-shift-x` or `ctrl-shift-x`) and verifying that "lean" is in the list of installed extensions:

![Extension Installed](images/lean_extension_installed.png)

Finally, you'll need to reload the VSCode window to get everything working. Open the Command Palette (`cmd-shift-p` or `ctrl-shift-p`) and select "Reload Window".

### Point the Lean mode extension to your Lean installation

Open User Settings by either pressing `cmd-,`/`ctrl-,` or by searching through the Command Palette.

Now copy the `lean.executablePath` path provided to you by `./leanup.py install` and create a new line in the editor on the right-hand side: 

```
"lean.executablePath": "/blah/blah/blah/leanup/lean_install/bin/lean",
```

It should look something like this:
![User Settings](/images/settings.png)

Hovering over the line should produce a tooltip indicating that VSCode is aware of its meaning to the Lean extension. Save the settings file and Reload Window once more for good measure.

### Test
When you are all done you should be able to open the file in `test/example.lean` and see some diagnostics.

![All Done!](/images/all_done.png)

Overall this process should take no more then a few minutes. I've done my best to test it on the major
platforms, if you have trouble please drop by the Slack channel `#505-au17` for questions/help.

### Common Installation issues:

- You receive a dynamic linking error due to missing a dependency such as `libgmp`.
- You receive a permission denied error due to installing Python in a directory you don't
  have permissions in, use `sudo your_command` instead.
- You did not reload VSCode after making changes to the set of extensions and the extension
  does not start, open Command Palette and run the `Reload Window` command or click on the blue
  button next to installed addons.

## Use

`leanup.py` has a one feature right now updating the Lean executables used by the class you can use `./leanup install`
to fetch a version, and `./leanup sync` to pull the latest version of the executable.
