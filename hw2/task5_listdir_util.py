import os
import sys
import stat
from prettytable import PrettyTable
from hw1.task4_file_size_conversion import file_size

if sys.platform == "win32":
    try:
        import win32api
        import win32security
        import pywintypes


        def get_windows_owner(file_path):
            sd = win32security.GetFileSecurity(file_path, win32security.OWNER_SECURITY_INFORMATION)
            owner_sid = sd.GetSecurityDescriptorOwner()
            owner = win32security.LookupAccountSid(None, owner_sid)[0]
            return owner


        def get_windows_group(file_path):
            sd = win32security.GetFileSecurity(file_path, win32security.GROUP_SECURITY_INFORMATION)
            group_sid = sd.GetSecurityDescriptorGroup()
            group = win32security.LookupAccountSid(None, group_sid)[0]
            return group
    except ImportError:
        win32api, win32security, pywintypes = None, None, None
else:
    try:
        import pwd
        import grp
    except ImportError:
        pwd, grp = None, None


def get_mode(file_stat):
    file_type = stat.filemode(file_stat.st_mode)
    return file_type


def get_owner(file_path, file_stat):
    if sys.platform == "win32" and win32security is not None:
        return get_windows_owner(file_path)
    elif pwd is not None:
        return pwd.getpwuid(file_stat.st_uid).pw_name
    else:
        return file_stat.st_uid


def get_group(file_path, file_stat):
    if sys.platform == "win32" and win32security is not None:
        return get_windows_group(file_path)
    elif grp is not None:
        return grp.getgrgid(file_stat.st_gid).gr_name
    else:
        return file_stat.st_gid


def get_size(file_stat):
    return file_size(file_stat.st_size)


def list_files(path="."):
    table = PrettyTable(["Mode", "Owner", "Group", "Size", "File Name"])
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        file_stat = os.stat(file_path)
        mode = get_mode(file_stat)
        owner = get_owner(file_path, file_stat)
        group = get_group(file_path, file_stat)
        size = get_size(file_stat)
        file_info = [mode, owner, group, size, file]
        table.add_row(file_info)
    print(table)


if __name__ == "__main__":
    list_files()
