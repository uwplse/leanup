The experince of using Lean will most likely be smoother using either Linux or macOS.

If you choose to use Windows you most likely already have `git`, `python`, and `pip`.

If you have such tools, and know what you are doing, feel free to ignore this advice.

If you are lost on how to get setup I would reconmend setting up [MSYS2](http://www.msys2.org/).

Once you have it installed you can use:

```
pacman -S git wget python
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install pipenv
pipenv install
```
