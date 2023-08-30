#!/usr/bin/env python
import sys
import argparse
import os
import fnmatch


def find(folder, name=None, show_dirs=True, show_files=True):
    """
    :param folder: path to a system folder from where to start searching
    :param name: file/directory name pattern, allows using '*' and '?' symbols
    :param show_dirs: if True - include directories into search results
    :param show_files: if True - include files into search results
    """
    pattern = '*' if name is None else name
    for root, dirs, files in os.walk(folder):
        if show_files:
            for filename in fnmatch.filter(files, pattern):
                print(os.path.join(root, filename))
        if show_dirs:
            for dirname in fnmatch.filter(dirs, pattern):
                print(os.path.join(root, dirname))


def parse_cmd_args():
    path_help = "Path to a folder"
    pattern_help = "File/directory name pattern. Allows using '*' and '?' symbols"
    type_help = "Where 'f' means search only files, 'd' means only directories"

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help=path_help)
    parser.add_argument('-name', nargs='?', default=None, help=pattern_help)
    parser.add_argument('-type', nargs='?', default=None, choices=['f', 'd'], help=type_help)

    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    cmd, _ = parser.parse_known_args()

    files, dirs = True, True
    if cmd.type == 'd':
        files = False
    if cmd.type == 'f':
        dirs = False
    return cmd.path, cmd.name, dirs, files


if __name__ == '__main__':
    args = parse_cmd_args()
    find(*args)
