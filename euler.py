#!/usr/bin/env python

import sys
import optparse
import time
import euler_util
try:
    import psyco
    psyco.full()
except ImportError:
    pass

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = optparse.OptionParser(
        formatter=optparse.TitledHelpFormatter(width=78),
        add_help_option=None)

    # define options here:
    #parser.add_option(
    #    '-h', '--help', action='help',
    #    help='Show this help message and exit.')

    settings, args = parser.parse_args(argv)

    # check number of arguments, verify values, etc.:
    if not args:
        print 'Specify the problem number to solve'
        return 1

    # import the function euler# and time its execution
    # if it does not exist, exit gracefully
    file_name = "euler%03d" % int(args[0])
    function_name = "euler%d" % int(args[0])
    try:
        module = __import__(file_name)
    except:
        print 'Could not import %s, has that problem been solved yet?'\
                % file_name
        raise
    invoke_function = getattr(module, function_name)
    if (callable(invoke_function)):
        print euler_util.trim(invoke_function.__doc__)
        start = time.time()
        try:
            print invoke_function()
        except:
            print 'Error during %s: %s' % (function_name, sys.exc_info()[0])
            raise

        end = time.time()
        print '%s took %0.0f ms' % (function_name, (end-start)*1000.0)
        return 0
    else:
        print '%s does not exist' % function_name
        return 1

if __name__ == "__main__":
    status = main()
    sys.exit(status)

