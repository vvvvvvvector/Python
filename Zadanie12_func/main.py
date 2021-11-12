def debug(seq):
    print("%s: %s" % (debug.__name__, seq))

def info(seq):
    print("%s: %s" % (info.__name__, seq))

def error(seq):
    print("%s: %s" % (error.__name__, seq))

def fatal(seq):
    print("%s: %s" % (fatal.__name__, seq))