#!/usr/bin/env python

import sys
import optparse
import time
import euler_util

def invoke(n, do_all):
    # import the function euler# and time its execution
    # if it does not exist, exit gracefully
    file_name = "euler%03d" % n
    function_name = "euler%d" % n
    try:
        module = __import__(file_name)
    except ImportError:
        if not do_all:
            print 'Could not import %s, has that problem been solved yet?'\
                % file_name
        return 1
    target_function = getattr(module, function_name)
    if not callable(target_function):
        if not do_all: print '%s does not exist' % function_name
        return 1

    if not do_all:
        print euler_util.trim(target_function.__doc__)
    start = time.time()
    try:
        if do_all:
            target_function()
        else:
            print target_function()
    except:
        print 'Error during %s: %s' % (function_name, sys.exc_info()[0])
        raise
    end = time.time()
    print '%s took %0.0f ms' % (function_name, (end - start) * 1000.0)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = optparse.OptionParser(
        formatter=optparse.TitledHelpFormatter(width=78),
        add_help_option=None)

    settings, args = parser.parse_args(argv)

    if not args:
        print 'usage: euler problem_number'
        return 1

    if args[0] == 'all':
        for i in range(1000):
            invoke(i, True)
        return 0
    else:
        return invoke(int(args[0]), False)

if __name__ == "__main__":
    status = main()
    sys.exit(status)
