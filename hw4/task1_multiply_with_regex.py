import re


def my_function(text, multiplier=2):
    return re.sub(r'\d+', lambda x: str(int(x.group()) * multiplier), text)
