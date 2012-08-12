#!/usr/bin/env python

import sys
import optparse
import time
import euler_util


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

    # import the function euler# and time its execution
    # if it does not exist, exit gracefully
    file_name = "euler%03d" % int(args[0])
    function_name = "euler%d" % int(args[0])
    try:
        module = __import__(file_name)
    except ImportError:
        print 'Could not import %s, has that problem been solved yet?'\
                % file_name
        return 1
    target_function = getattr(module, function_name)
    if not callable(target_function):
        print '%s does not exist' % function_name
        return 1

    print euler_util.trim(target_function.__doc__)
    start = time.time()
    try:
        print target_function()
    except:
        print 'Error during %s: %s' % (function_name, sys.exc_info()[0])
        raise
    end = time.time()
    print '%s took %0.0f ms' % (function_name, (end - start) * 1000.0)
    return 0

if __name__ == "__main__":
    status = main()
    sys.exit(status)
