class StreamHandler(object):
    def __init__(self, fp):
        self.fp = fp

    def __call__(self, msg):
        print >>self.fp, msg
        pass


class FileHandler(object):
    def __init__(self, filename):
        self.filename = filename
        self.fp = open(self.filename, 'w+')

    def __call__(self, msg):
        print >>self.fp, msg
        pass
