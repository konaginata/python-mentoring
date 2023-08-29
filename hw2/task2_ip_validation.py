import re
import socket


def check_ip_regex(ip_address: str) -> bool:
    pattern = "^(([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]).){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$"
    return bool(re.match(pattern, ip_address)) if isinstance(ip_address, str) else False


def check_ip_socket(ip_address: str) -> bool:
    try:
        socket.inet_aton(ip_address)
        return True
    except (ValueError, TypeError, socket.error):
        return False


tests = [
    ("", False),
    ("192.168.0.1", True),
    ("0.0.0.1", True),
    ("10.100.500.32", False),
    (700, False),
    ("127.0.1", True)
]
for address, expected in tests:
    assert check_ip_regex(address) == expected
    assert check_ip_socket(address) == expected
