# Generate DocStrings for ULB Projects

With this script, you can easily generate pretty decent docstrings for your python projects. It will store your created profiles in `~/.gendocstring` to save you some time.

## Installation

### Dependencies

You need to have `python3` and `xclip` installed on your system.
```bash
sudo apt install python3 xclip
```

### Install Script

```bash
curl -s https://raw.githubusercontent.com/F2Ville/gendocstring/master/install.sh | bash
```

## Usage
You can use the script with `--copy` to copy the generated docstring to your clipboard.
```bash
gendocstring
# or
gendocstring --copy
```