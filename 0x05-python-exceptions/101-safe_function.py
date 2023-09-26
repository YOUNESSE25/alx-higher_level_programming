#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(*args)
        return a
    except Exception as n:
        print("Exception: {}".format(n), file=sys.stderr)
        return None
