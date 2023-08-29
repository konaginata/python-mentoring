import os
import fnmatch
import argparse


def find_util(root_dir, pattern="*", file_type="all"):
    items_found = []
    for root, dirs, files in os.walk(root_dir):
        for name in files + dirs:
            if fnmatch.fnmatch(name, pattern):
                if file_type == "d" and not os.path.isdir(os.path.join(root, name)):
                    continue
                elif file_type == "f" and not os.path.isfile(os.path.join(root, name)):
                    continue
                items_found.append(os.path.join(root, name))
        return items_found


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search tool for files and directories")
    parser.add_argument("root_dir", help="root directory for search", type=str)
    parser.add_argument("-name", help="item name pattern", default="*")
    parser.add_argument("-type", help="item type: f (file) || d (directory) || all (both) as default",
                        choices=["f", "d", "all"], default="all")
    args = parser.parse_args()
    items = find_util(args.root_dir, args.name, args.type)
    for item in items:
        print(item)
