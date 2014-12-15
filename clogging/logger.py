from .constants import LOG_DEBUG, LOG_INFO, LOG_WARN, LOG_ERROR


def noob(msg, *args):
    if not args:
        return msg
    else:
        return msg % args


class Logger(object):
    def __init__(self, level, handler, formatter):
        self.level = level
        self.handler = handler
        self.formatter = formatter or noob

    def log(self, level, *args, **kwargs):
        if self.level < level:
            return
        self.handler(self.formatter(*args, **kwargs))

    def debug(self, *args, **kwargs):
        self.log(LOG_DEBUG, *args)

    def info(self, *args, **kwargs):
        self.log(LOG_INFO, *args)

    def warn(self, *args, **kwargs):
        self.log(LOG_WARN, *args)

    def error(self, *args, **kwargs):
        self.log(LOG_ERROR, *args)
