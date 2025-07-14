import re
regex = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$'


def fun(s):
    if (re.fullmatch(regex, s)): return True
    else: return False
    # return True if s is a valid email, else return False


def filter_mail(emails):
    return sorted(list(filter(fun, emails)))


