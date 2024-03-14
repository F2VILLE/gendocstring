#!/bin/sh
if [ -f /usr/local/bin/gendocstring ]; then
    echo "gendocstring is already installed. Exiting."
    exit 1
fi

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "Installing gendocstring..."

curl -s https://raw.githubusercontent.com/F2Ville/gendocstring/master/gendocstring.py > /usr/local/bin/gendocstring

chmod +x /usr/local/bin/gendocstring

echo "gendocstring installed successfully !"
echo .
echo "(You may need to restart your terminal to use gendocstring.)"