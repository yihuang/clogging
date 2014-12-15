import sys
from .handlers import StreamHandler
from .logger import Logger
from .constants import LOG_INFO

level_config = {}
handle_config = {}
formatter_config = {}


def getLogger(name='root', level=None, handler=None, formatter=None):
    level = level or level_config.get(name, LOG_INFO)
    handler = handler or handle_config.get(name) or StreamHandler(sys.stderr)
    formatter = formatter or formatter_config.get(name)
    return Logger(level, handler, formatter)
