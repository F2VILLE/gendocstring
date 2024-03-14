# Generate DocStrings for ULB Projects
*(This script is made for linux. Only tested on Ubuntu 22.04 with Python 3.10.12)*
With this script, you can easily generate pretty decent docstrings for your python projects. It will store your created profiles in `~/.gendocstring` to save you some time.

### Example
```python
"""
     Lesson               : INFO-F-101
     Project name         : Minesweeper
     Author               : John Doe
     Email                : john.doe@ulb.be
     Matricule            : 000123456
"""
```

## Installation

### Dependencies

You need to have `python3` and `xclip` installed on your system.
```bash
sudo apt install python3 xclip
```

### Install Script

```bash
curl -s https://raw.githubusercontent.com/F2Ville/gendocstring/master/install.sh | sudo bash
```

## Usage
You can use the script with `--copy` to copy the generated docstring to your clipboard. \
*/!\\ `--copy` option requires `xclip` to be installed on your system, and it is **not already implemented**. It is planned for the next release.*
```bash
gendocstring
# or
gendocstring --copy
```

# TODO

- [ ] Implement `--copy` option
- [ ] Add support for other OS
- [ ] Implement `<file>` option to directly write the docstring in a file (For: Python, C, C++, JS, Bash)