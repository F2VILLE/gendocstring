#!/bin/sh
curl -s https://raw.githubusercontent.com/F2Ville/gendocstring/master/gendocstring.py > /usr/local/bin/gendocstring

chmod +x /usr/local/bin/gendocstring

echo "gendocstring installed successfully !"
echo .
echo "(You may need to restart your terminal to use gendocstring.)