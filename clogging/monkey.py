import sys


def patch():
    import clogging
    sys.modules['logging'] = clogging
