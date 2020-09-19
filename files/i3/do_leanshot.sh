#!/bin/bash
set -e
maim -s -u | xclip -selection clipboard -t image/png -i
